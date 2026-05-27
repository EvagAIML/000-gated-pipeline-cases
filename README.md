# 000-gated-pipeline-cases

Case studies demonstrating the [Gated Pipeline](https://github.com/EvagAIML/gated-pipeline) ML lifecycle harness in action. Each case study is a Colab notebook that runs end-to-end, downloads its data automatically, and produces the demo's outputs.

## How it works

On every push to `main`, GitHub Actions:
- Converts each notebook in `/notebooks/**` into a static HTML page
- Publishes a homepage index listing all case studies
- Creates downloadable artifacts per case study:
  - notebook.html
  - notebook.ipynb
  - notebook.py (if present)
  - assets/ (if present)
- Emits a one-click "Run in Colab" URL into each card

## Repo structure

- `notebooks/<case-study-slug>/` contains your source notebooks
- `notebooks/_shared/data_access.py` is the shared dataset loader (manifest + SHA-256 verified)
- `dataset_manifest.json` maps each slug to a dataset URL in the sibling `-data` repo
- `site/` is generated during Actions (do not edit manually; gitignored)

Naming convention:
`what-problem__problem-type__model-family-or-study`
(lowercase, hyphens inside segments, double underscores between segments)

## Live published index

https://evagaiml.github.io/000-gated-pipeline-cases/

## Related repos

- [`gated-pipeline`](https://github.com/EvagAIML/gated-pipeline) — the harness itself (one Python file, CI-asserted gates)
- [`000-gated-pipeline-cases-data`](https://github.com/EvagAIML/000-gated-pipeline-cases-data) — versioned dataset zips for the case studies

## Contributing

See `CONTRIBUTING.md` (to be added) for the procedure to add or update a case study.
