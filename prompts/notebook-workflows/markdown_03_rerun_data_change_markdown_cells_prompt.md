# Markdown 03 — Rerun Data Change Markdown Cells Prompt

Use the current saved notebook code and outputs as the source of truth.

I do not want a full notebook rewrite.
Only identify and update markdown cells whose factual claims changed because of the latest rerun.

Source priority:
1. Attached .ipynb / .py files
2. HTML for rendered outputs

Task:
1. Check all existing markdown cells that sit directly above code cells.
2. Identify only the cells whose numeric claims, selected configuration, or run-specific statements no longer match the saved outputs.
3. Leave unchanged any markdown cell that is still accurate.
4. Return edits in top-to-bottom order using this format only:
   - Replace the cell titled "..."
   - When you reach the cell titled "...", delete it
   - Insert a new markdown cell directly above the code cell titled "..."

Rules:
- The markdown title must match the code-cell title exactly.
- Use:
  - **Process:**
  - **Analysis:** only when needed
  - **Outcome:**
- Keep each markdown cell short, executive-readable, and technically useful.
- Any data cited must match the current saved outputs exactly.
- If nothing needs to change for a cell, do not mention it.
- Do not update the first or last summary cells in this pass.
- If a needed output is missing or unclear, ask before writing it.

Double-check requirement:
- Compare the current notebook against the previously completed version and confirm whether the markdown still aligns in structure, tone, and level of detail.
- If anything significant changed in the rerun—such as the best model, selected configuration, score pattern, dataset size, or notable failure mode—explicitly call it out in the replacement text.
- If no significant differences exist, do not manufacture them.

Return only the cells that need to be changed.
