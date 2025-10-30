Title: docs(README): add “Useful git commands” quick reference

Overview
This PR updates the README to improve onboarding by adding a quick-reference section for common Git commands. It complements the existing PATH configuration note and provides a minimal workflow for staging and committing changes.

What changed
- Added a new section: “Useful git commands”
  - git status
  - git add FILE1 FILE2
  - git commit -m "Description of my new code changes"
- Added spacing after the PATH setup line to improve readability.
- No code, build, or dependency changes.

Why
- New contributors often need a quick reminder of the basic Git workflow right in the project README.
- Reduces friction for first-time contributors and standardizes commit practices.

Impact
- Documentation-only change; no runtime impact.

Verification
- Previewed README to confirm proper Markdown rendering and bullet formatting.
- Confirmed the existing PATH instruction remains unchanged.

Notes
- The file currently has no trailing newline; can be addressed in a follow-up if desired.