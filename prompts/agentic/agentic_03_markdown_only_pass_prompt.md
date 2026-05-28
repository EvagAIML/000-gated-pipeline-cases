# Agentic 03 — Markdown Only Pass Prompt

Treat this as a controlled, notebook-aware markdown refactor for one notebook only.

Use the current saved notebook code and outputs as the source of truth.

Source priority:
1. The notebook `.ipynb` file for exact cell order, markdown placement, and saved outputs
2. The notebook `.py` export for readable code and markdown content
3. HTML only as a secondary reference for rendered outputs and visual confirmation

## Objective

Standardize one notebook’s markdown so it matches the project notebook workflow.

This includes, in order:
1. markdown cells directly above code cells
2. the first notebook markdown cell
3. the last notebook markdown cell

Do this for one notebook only.
Do not process multiple notebooks in this run.

## Non-Negotiable Rules

1. Do not change executable code.
2. Do not remove executable code.
3. Do not reorder executable code.
4. Do not rename variables, functions, classes, models, files, datasets, columns, paths, or parameters.
5. Do not split or merge notebook cells.
6. Preserve notebook order.
7. Any numeric or run-specific claim must match the current saved outputs exactly.
8. If required output is missing, unclear, stale, or contradictory, stop and ask rather than guessing.
9. If a cell cannot be safely standardized, skip it and report it.

## Phase 1 — Pre-Code Markdown Cells

Only update markdown cells that sit directly above the code cells they describe.

Rules:
- work top to bottom through the notebook
- the markdown title must match the code-cell title exactly as written in the notebook
- use this structure:
  - **Process:**
  - **Analysis:** only when interpretation is needed
  - **Outcome:**
- keep each markdown cell short, high value, executive-readable, and technically useful
- do not add filler
- do not repeat obvious code details
- omit **Analysis** for simple setup or utility cells when it adds no value

For tuning or comparison cells, explicitly include:
- what was being determined
- what the different settings showed
- what was chosen and why

If there are old markdown cells that are no longer needed because their purpose is now covered by the pre-code markdown structure, delete them inline as you move downward through the notebook.

## Phase 2 — First and Last Notebook Cells

After the pre-code markdown cells are complete, update:
1. the first notebook markdown cell
2. the last notebook markdown cell

Requirements:
- preserve existing structure unless a factual update is required
- update all run-dependent claims to match the current saved outputs exactly
- include the actual data file name in the Data Description section when appropriate
- use a positive but accurate framing in performance sections
- include deployment or integration implications only if supported by the notebook outcomes
- if relevant, call out meaningful deployment implications such as integration paths, operational usefulness, or resource-focusing benefits
- do not invent claims, metrics, or recommendations

## Cross-Notebook Consistency Check

Compare the notebook against the previously completed project notebook and keep these aligned unless the notebook’s actual results require a real difference:
- structure
- tone
- brevity
- level of detail
- section naming style

If something significant changed, explicitly call it out rather than forcing artificial consistency. Examples:
- a different model performed best
- a different configuration was selected
- score patterns changed materially
- the dataset or file changed
- deployment implications changed

## Validation

Before finalizing:
1. confirm executable code was not changed
2. confirm code-cell titles and markdown titles align exactly where required
3. confirm all numeric claims match the current saved outputs
4. confirm first and last cells align with the finalized pre-code markdown cells
5. confirm any significant differences from the previous notebook are explicitly called out
6. report any skipped cells and why

## Return Format

Return:
1. a concise summary of what was updated
2. the list of notebook cells changed, in top-to-bottom order
3. any cells skipped
4. any significant differences called out
5. a validation statement confirming what was and was not changed

## Important

This is a one-notebook markdown-only prompt.
Do not broaden scope beyond this notebook.
Prefer minimal, correct changes over aggressive rewriting.
