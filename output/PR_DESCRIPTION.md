Title: Secure OpenAI credentials via environment variables (.env); keep recent CLI and API upgrades

Summary:
This PR removes the previously hard-coded OpenAI API key and switches to environment-based configuration with python-dotenv. It preserves the recent improvements to the CLI (auto-generating diffs via git) and the migration to the Chat Completions API.

What changed:
- Security/configuration
  - Added dotenv support and call load_dotenv() at startup.
  - Read API key from environment via KEY.
  - Note: client initialization currently passes an empty string to OpenAI(api_key=""). This is a bug; it must pass the loaded api_key or rely on the library’s default env lookup.
- Context (from recent changes retained)
  - Optional --diff flag; when omitted, auto-generates a diff using git diff and writes it to input/diff.txt.
  - Uses client.chat.completions.create with messages instead of Responses API.
  - Simplified I/O by removing legacy encoding fallbacks and dotenv dependency was reintroduced only for credentials.
  - Removed previously committed generated artifacts (input/diff.txt, output/PR_DESCRIPTION.md, output/PR_DESCRPTION.md).

Why:
- Eliminate the security risk of a hard-coded API key and enable safer, environment-based configuration.
- Maintain the improved UX for generating PR descriptions without manually preparing diff files.
- Align with modern OpenAI API usage (chat-based).

Impact:
- Behavior:
  - The tool now expects an API key to be provided via environment (e.g., .env). Without it, authentication will fail.
- Risk/known issue:
  - As written, client = OpenAI(api_key="") will always fail. Must be updated to client = OpenAI(api_key=api_key) or allow the SDK to read from OPENAI_API_KEY automatically.
  - Prior removal of robust text-decoding fallbacks may still affect non-UTF-8 diffs.

How to test:
- With a .env file or exported environment variable:
  - Set KEY=<your_api_key> (or use OPENAI_API_KEY if switching to the standard name).
  - In a repo with local changes, run: python src/main.py --output output/PR_DESCRIPTION.md
    - Expect: git diff runs, input/diff.txt is created, and a PR description is written.
  - With an explicit diff: python src/main.py --diff path/to/diff.txt --output output/PR_DESCRIPTION.md
    - Expect: provided diff is used; no git invocation.
- Verify that the description content is generated and no authentication errors occur.

Security considerations:
- The previously exposed API key must be revoked/rotated immediately if not already.
- Ensure no secrets are committed going forward; rely on environment variables (.env ignored by VCS).

Follow-ups:
- Fix client initialization: client = OpenAI(api_key=api_key) and fail fast if api_key is missing; consider standardizing on OPENAI_API_KEY for compatibility with tooling.
- Optionally restore robust text decoding or enforce UTF-8 throughout and write files with explicit UTF-8 + LF.
- Add a staged-only mode (git diff --staged) and basic tests for get_diff and generation flow.

Changelog:
- Security: remove hard-coded OpenAI key; load from env via dotenv.
- CLI: retain optional --diff with auto-generated git diff.
- OpenAI: continue using Chat Completions API.
- Repo hygiene: keep generated artifacts out of version control.