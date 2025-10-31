Title: Expand README with basic Git quick-start commands

Summary:
This PR enhances the README to better support new contributors by adding a concise "Useful git commands" section. It also keeps the existing Windows-specific note for adding Git to PATH via PowerShell.

What changed:
- Added a new section: "Useful git commands"
  - git status
  - git add FILE1 FILE2
  - git commit -m "Description of my new code changes"
- Preserved the existing PowerShell line for adding Git to PATH on Windows: $env:Path += ";C:\Program Files\Git\cmd"
- Improved readability with headers and spacing.

Why:
- Provide a quick reference for common Git tasks to streamline onboarding and daily workflows.
- Make the README more immediately useful for contributors who are new to Git or this repository’s workflow.

Impact:
- Documentation-only change; no code or build impact.
- Low risk.

Follow-ups (optional):
- Add commands for branching, pulling/pushing, and reviewing history.
- Separate platform-specific setup guidance (Windows/macOS/Linux) into their own subsections.