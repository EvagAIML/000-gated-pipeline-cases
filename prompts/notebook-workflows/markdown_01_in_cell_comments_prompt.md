# Markdown 01 — In-Cell Comments Prompt

Treat this as a non-functional refactor with zero executable diffs allowed.

Use the current saved notebook code as the source of truth.

Task:
Standardize comments inside code cells for one notebook.

Scope:
- Update code cells only
- Do not rewrite markdown cells
- Do not change executable Python code
- Do not change outputs
- Do not split or merge cells

Rules:
1. Do not change executable code.
2. Do not reorder code.
3. Do not add, remove, or alter imports.
4. Do not rename variables, functions, classes, models, files, datasets, columns, paths, or parameters.
5. Only add comments and optional blank lines.
6. Preserve notebook cell order and structure.

Required code-cell style:
1. At the top of each code cell, add a title using this exact structure:

    # ------------------------------
    # <CELL TITLE IN ALL CAPS>
    # ------------------------------

2. The title must match the primary purpose of the code cell.
3. Add 1 to 3 short purpose comments below the title.
4. If the cell contains imports:
   - add a short import-purpose comment block above the import lines
   - explain what each library or module is used for in that cell
5. Add short section comments above major logical blocks inside the cell.
6. When a section uses an imported library or module, mention that import again in the section comment with more specific detail.

Style:
- Major titles in ALL CAPS
- Comments in sentence case
- Short, clear, professional wording
- Prefer purpose over syntax restatement

Validation:
1. Compare original and updated code cells after removing comment-only lines and formatting-only blank lines.
2. Confirm that executable code is identical.
3. Skip any cell that cannot be safely updated without risk.

Return:
- a summary of cells updated
- any skipped cells
- confirmation that executable code was preserved
