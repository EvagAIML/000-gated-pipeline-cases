# Markdown 02 — Pre-Code Markdown Cells Prompt

Use the current saved notebook code and outputs as the source of truth.

Source priority:
1. Attached .ipynb / .py files for exact cell order, code-cell titles, and markdown placement
2. HTML for rendered outputs and visible execution results

We are only updating markdown cells that sit directly above the code cells they describe.
Do not update the first or last summary cells in this pass.

Rules:
1. Work top to bottom through the notebook so I can move down the document without jumping around.
2. Give instructions in this format only:
   - Replace the cell titled "..."
   - When you reach the cell titled "...", delete it
   - Insert a new markdown cell directly above the code cell titled "..."
3. The markdown title must match the code-cell title exactly as written in the notebook.
4. Use this structure:
   - **Process:**
   - **Analysis:** only when interpretation is needed
   - **Outcome:**
5. Keep each markdown cell short, high value, executive-readable, and technically useful.
6. Any data cited must match the current saved outputs, not earlier notebook text.
7. For tuning or comparison cells, include:
   - what was being determined
   - what the different settings showed
   - what was chosen and why
8. Do not give a separate cleanup list. Put deletions inline as I move down the notebook.
9. If any output needed for a markdown cell is missing or unclear, ask before writing it.
10. Do not rewrite code cells.

Cross-notebook consistency check:
11. Compare formatting, structure, and tone against the previously completed notebook so they remain aligned.
12. If something significant changed—such as the best model, best configuration, score pattern, dataset, or deployment implication—explicitly call it out in the relevant markdown cell.

Style guidance:
- Prefer tight wording over filler.
- Do not repeat obvious information already visible in the code.
- Analysis should explain the implication or decision, not restate the process.
- Omit Analysis for simple setup or utility cells when it adds no value.

Return only the step-by-step notebook edits.
