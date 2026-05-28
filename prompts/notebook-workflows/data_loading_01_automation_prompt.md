# Data Loading 01 — Automation Prompt

Use the current notebook code, outputs, and project conventions as the source of truth.

Task:
Refactor the environment setup, dependency installation, and dataset-loading workflow so it is reliable, repeatable, and user-friendly in Google Colab.

Goals:
1. Install dependencies only when needed.
2. Clearly notify the user when a runtime restart is required.
3. Avoid repeated reinstalls after restart.
4. Avoid stale cached dataset artifacts from prior runs.
5. Load notebook-specific datasets in a repeatable way.
6. Keep the workflow simple enough for long-running notebooks.

Requirements:
1. Preserve the notebook’s intended behavior.
2. Use a persistent flag to detect whether dependencies were already installed.
3. If dependencies are newly installed:
   - install them quietly where possible
   - create the install flag
   - render a clear HTML or notebook-visible message telling the user to restart the runtime and run all cells again
4. If dependencies are already installed:
   - print a short success message
   - do not prompt for restart
5. Separate dependency setup from shared imports when practical.
6. For dataset loading:
   - use a notebook-specific slug or identifier
   - clear stale notebook-specific cached dataset artifacts once per fresh session
   - download any shared helper file only when needed
   - load the dataset into a deterministic notebook-specific directory
7. Use notebook-friendly visible output so the user knows:
   - whether dependencies were installed
   - whether restart is required
   - whether the dataset was found and loaded
8. Avoid brittle hardcoded paths when possible.
9. Keep the code idempotent so rerunning cells does not corrupt state.
10. Do not modify unrelated model, training, retrieval, or evaluation code.

Implementation guidance:
- Prefer a setup pattern with:
  - environment flags
  - a dependency-installed flag file
  - a one-time session cache refresh flag
  - notebook-specific cache folders
- Prefer safe cleanup of only notebook-specific cached artifacts.
- Keep printed status messages short and explicit.
- Use HTML output for restart-required notices when helpful.

Validation:
1. Confirm that a fresh runtime installs dependencies and shows a restart-required message.
2. Confirm that after restart, the install cell does not reinstall dependencies.
3. Confirm that stale notebook-specific cached artifacts are cleared only once per fresh session.
4. Confirm that dataset loading succeeds and reports what was loaded.
5. Report any assumptions or notebook-specific paths introduced.

Return:
- the updated setup / data-loading code
- a short summary of what changed
- any notebook-specific values that must be customized
