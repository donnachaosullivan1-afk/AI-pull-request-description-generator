Title: README: add quick-start Git commands for contributors

Summary:
This PR expands the README with a concise “Useful git commands” section to help new contributors get started. It complements the existing PowerShell PATH instruction for Git by adding common commands used in a basic workflow.

What changed:
- Added a “Useful git commands” section to README.md
- Included examples for:
  - git status
  - git add FILE1 FILE2
  - git commit -m "Description of my new code changes"
- Preserved the existing PowerShell PATH update for Git and added spacing for readability

Why:
- Improve onboarding by providing an immediate, copy-pastable reference for everyday Git tasks
- Reduce friction for contributors who may be new to Git
- Make the README more self-contained for quick setup and first commits

Impact:
- Documentation-only; no code or runtime changes

Follow-ups (optional):
- Add commands for git push, git pull, and branching
- Include macOS/Linux equivalents for PATH setup
- Link to a CONTRIBUTING.md with a fuller workflow and commit message guidelines