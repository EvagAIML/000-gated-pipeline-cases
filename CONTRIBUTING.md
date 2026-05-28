# Contributing — Case Studies for the Gated Pipeline

How to add or update a case study notebook in this repo.

## Repo layout

- `notebooks/<slug>/<slug>.ipynb` — the case study notebook (one folder per case study).
- `notebooks/_shared/data_access.py` — the shared dataset loader. Notebooks import `ensure_dataset(slug)` from here.
- `notebooks/failed/<slug>/<slug>.ipynb` — failed experiments preserved for learning (separate subtree).
- `dataset_manifest.json` — maps each slug to a versioned dataset zip in the sibling [`-data` repo](https://github.com/EvagAIML/000-gated-pipeline-cases-data).
- `.github/workflows/build.yml` — converts each `.ipynb` to HTML, builds the homepage, deploys to GitHub Pages.
- `prompts/` — reusable authoring prompts (see below).
- `site/` — generated during Actions (gitignored; do not edit).

## Slug naming

```
what-problem__problem-type__model-family-or-study
```

All lowercase. Hyphens inside segments. Double underscores between segments. Examples:

- `leak-detection__regression__gated-harness`
- `co-target-detection__regression__reconstruction-scan`

## Add a new case study

1. Pick the slug.
2. Create `notebooks/<slug>/`.
3. Stage the dataset zip in the [`-data` repo](https://github.com/EvagAIML/000-gated-pipeline-cases-data) as `<slug>__dataset__v1.zip`. The zip's internal layout should produce a top-level folder matching the `extract_to` value:
   ```
   <slug>__dataset__v1/
   └── raw/
       └── <your-csv-files>
   ```
4. Compute the zip's SHA-256: `shasum -a 256 <zip-file>`.
5. Add the manifest entry to `dataset_manifest.json`:
   ```json
   "<slug>": {
     "url": "https://raw.githubusercontent.com/EvagAIML/000-gated-pipeline-cases-data/main/<slug>__dataset__v1.zip",
     "sha256": "<computed-sha>",
     "extract_to": "<slug>__dataset__v1"
   }
   ```
6. Author the notebook at `notebooks/<slug>/<slug>.ipynb` following the structure below.
7. Test from a fresh kernel: `papermill notebooks/<slug>/<slug>.ipynb /tmp/<slug>-executed.ipynb`. Papermill must exit 0.
8. Clear outputs in the source `.ipynb` before commit (`jupyter nbconvert --clear-output --inplace notebooks/<slug>/<slug>.ipynb`).
9. Commit to `main`. The build workflow publishes the new case study.

## Notebook structure (Section 1–4)

Every case study notebook follows the same four-section structure:

1. **Title + Value Proposition + Executive Summary.** One-paragraph value prop naming the problem, the solution, the headline metric, and the dollar impact. Business Opportunities (A, B, C — Opportunity/Solution pairs). Outcomes block with Model Performance, Architecture, Economic Impact, Strategy Recommendation (Enterprise + SMB split).
2. **Problem Space.** Overview (why the problem matters; costs of being wrong in each direction). Data Description (row counts, target, class balance). Process (data prep, modeling, evaluation in one sentence each). Results table with the winning model marked `✅`.
3. **Code Execution.** Runtime Configuration block + dependency-install cell (with the runtime-restart HTML notice if `!pip install` runs) + the work itself. Every code cell has a markdown cell directly above it with `**Process:**`, optional `**Analysis:**`, `**Outcome:**` — and the markdown title matches the code cell's ALL-CAPS banner exactly. The code cell has a banner + 1–3 purpose comments + section comments above major logical blocks.
4. **Expanded Executive Summary.** TLDR (one or two paragraphs naming the winning model and the dollar impact) + Full Summary (Objective / Iterative Development / Performance Analysis / Economic Impact / Deployment Readiness / Next Steps).

Section 3's grouping varies. Use Layout A (sequential `###` subheadings) by default. Use Layout B (multi-phase `##` groupings) only when the work has 3+ distinct phases — RAG pipelines, multi-stage retrieval, etc.

## The Colab-replicable contract

The notebook MUST run end-to-end in a fresh Colab kernel:

- Dependencies install in the first code cell via `!pip install`. Assume nothing about the runtime's pre-installed packages.
- No hardcoded local paths. Use `ensure_dataset(slug)` from `_shared/data_access.py` for data.
- No hidden state across cells. A reader running cell N must be able to see everything cell N depends on in cells 1 through N–1.
- One logical step per code cell. If you have to use the word "and" to describe what a cell does, split it.
- Markdown cells explain WHY each step exists. Code shows what; markdown says why.

If `papermill <input>.ipynb <output>.ipynb` from a clean venv fails, the notebook is not ready to commit.

## Failed experiments

Failed experiments live at `notebooks/failed/<slug>/<slug>.ipynb`. They follow the same Section 1–4 structure with failure-appropriate reframing:

- Section 1 carries a `⚠️ FAILED EXPERIMENT` marker in the title + a "preserved for learning" callout + Hypothesis (with the explicit success threshold) + Failure Summary (five bullets: what broke / the signal / the root cause / what this teaches / whether to retry).
- Section 3 marks the failure point explicitly: `### <Step Name> (FAILURE POINT)`.
- Section 4 is Failure Analysis: TLDR + Full Analysis (Objective / Hypothesis Grounding / Where It Broke / Why It Broke / What I Tried / What This Teaches / What I'd Do Differently).

Failed experiments publish alongside successful case studies on a separate section of the homepage, with a visual marker so they aren't confused with deployable results.

## Authoring prompts

The `prompts/` directory contains the reusable authoring prompts ported from the [`000-website-notebooks`](https://github.com/EvagAIML/000-website-notebooks) reference repo:

- `prompts/notebook-workflows/` — the four-stage human-runnable workflow (in-cell comments, pre-code markdown, rerun deltas, first/last cells) plus the data-loading automation prompt.
- `prompts/agentic/` — the agentic single-pass version that runs Phase 2 + Phase 4 in one LLM run.

Use the agentic prompt when an LLM is doing the markdown work end-to-end; use the four stages when iterating manually.

## Voice

The notebooks are professional ML engineering work. Write in a direct, headline-first voice. Avoid:

- Hedge phrases ("it's worth noting," "importantly," "indeed")
- AI-favored vocabulary ("leveraging," "comprehensive," "robust," "seamless," "delve into")
- Tutorial voice ("let's dive in," "now we'll explore")
- Excessive em-dashes
- Marketing tone in technical content

The structure does the work. Write the structure cleanly and let it land.

## Update an existing case study

1. Edit `notebooks/<slug>/<slug>.ipynb`.
2. If the dataset changed, bump the data repo's zip filename to `<slug>__dataset__v<N+1>.zip`, then update the manifest's `url`, `sha256`, and `extract_to` fields.
3. Test from a fresh kernel via papermill.
4. Clear outputs.
5. Commit to `main`. URLs do not change.

## Do not

- Edit the `gh-pages` branch by hand. Every push to `main` overwrites it.
- Commit `site/` — it's a build artifact.
- Commit notebooks with cell outputs. The `.html` artifact (built by Actions) carries the rendered version.
- Put notebooks at repo root. The build workflow's `find notebooks` won't find them.
- Hardcode local paths. Use `ensure_dataset(slug)`.

## Troubleshooting

If the build workflow fails: Actions → Build Notebooks → open the failed step. Common issues:

- Folder slug and notebook base name don't match exactly.
- Wrong capitalization.
- Missing `.ipynb` in a case-study folder.
- Notebook errors at runtime (rerun papermill locally, fix, re-push).
- Dataset SHA mismatch (the `ensure_dataset` loader raises `ValueError` — verify the manifest entry against `shasum -a 256` of the zip in the data repo).
