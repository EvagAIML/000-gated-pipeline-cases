import hashlib
import json
import sys
import urllib.request
import zipfile
from pathlib import Path


REPO_OWNER = "EvagAIML"
CODE_REPO = "000-gated-pipeline-cases"
MANIFEST_URL = f"https://raw.githubusercontent.com/{REPO_OWNER}/{CODE_REPO}/main/dataset_manifest.json"


def _in_colab() -> bool:
    return "google.colab" in sys.modules


def _cache_root() -> Path:
    return Path("/content/data_cache") if _in_colab() else Path("./data_cache")


def _load_manifest() -> dict:
    local_manifest = Path("dataset_manifest.json")
    if local_manifest.exists():
        return json.loads(local_manifest.read_text(encoding="utf-8"))

    with urllib.request.urlopen(MANIFEST_URL) as response:
        return json.loads(response.read().decode("utf-8"))


def _sha256(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_extract(zip_path: Path, dest_dir: Path) -> None:
    with zipfile.ZipFile(zip_path, "r") as zf:
        for member in zf.infolist():
            member_path = dest_dir / member.filename
            resolved = member_path.resolve()
            if not str(resolved).startswith(str(dest_dir.resolve())):
                raise ValueError(f"Unsafe path in zip: {member.filename}")
        zf.extractall(dest_dir)


def ensure_dataset(slug: str) -> Path:
    manifest = _load_manifest()

    if slug not in manifest:
        raise KeyError(
            f"No dataset manifest entry found for '{slug}'. "
            f"Add it to dataset_manifest.json."
        )

    entry = manifest[slug]
    url = entry["url"]
    expected_sha = entry.get("sha256", "").strip()
    extract_to = entry.get("extract_to", slug)

    cache_root = _cache_root()
    cache_root.mkdir(parents=True, exist_ok=True)

    dataset_dir = cache_root / extract_to
    ready_marker = dataset_dir / ".ready"

    if ready_marker.exists():
        return dataset_dir

    zip_name = url.split("/")[-1]
    zip_path = cache_root / zip_name

    if not zip_path.exists():
        print(f"Downloading dataset for '{slug}'...")
        urllib.request.urlretrieve(url, zip_path)

    if expected_sha:
        actual_sha = _sha256(zip_path)
        if actual_sha != expected_sha:
            raise ValueError(
                f"SHA256 mismatch for {zip_name}. "
                f"Expected {expected_sha}, got {actual_sha}"
            )

    print(f"Extracting dataset for '{slug}'...")
    _safe_extract(zip_path, cache_root)

    if not dataset_dir.exists():
        raise FileNotFoundError(
            f"Expected extracted dataset folder '{dataset_dir}' was not found."
        )

    ready_marker.touch()
    return dataset_dir
