# Markdown 04 — First and Last Markdown Cells Prompt

Use the current saved notebook code and outputs as the source of truth.

Source priority:
1. Attached .ipynb / .py files
2. HTML for rendered outputs

Only update:
1. the first notebook markdown cell
2. the last notebook markdown cell

Do not change any other cells.

Requirements:
1. Preserve the existing structure and tone unless a factual update is required.
2. Update all run-dependent claims so they match the latest saved outputs exactly.
3. Include the actual data file name in the Data Description section when appropriate.
4. In the performance section, use a positive but accurate framing.
5. If relevant to the notebook, include deployment or integration implications supported by the project outcomes.
6. Do not invent numbers or claims.
7. Keep the writing concise and polished.

Cross-check requirement:
8. Double-check that the first and last cells align with the pre-code markdown cells already finalized for this notebook.
9. Double-check that they also align in tone, structure, and presentation with the previous completed notebook.
10. If something significant changed—such as the best model, best configuration, score pattern, data source, or deployment recommendation—explicitly call that out rather than carrying over older framing.

Return:
- Replace the first cell with:
  <full markdown>
- Replace the last cell with:
  <full markdown>
