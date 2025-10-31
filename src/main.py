#!/usr/bin/env python3
import argparse
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pr_description(diff: str) -> str:
    api_key = os.getenv("KEY")
    client = OpenAI(api_key=api_key)

    prompt = f"""
You are a helpful assistant that generates PR descriptions.
Here is the diff of what changed:

{diff}

Write a clear and helpful pull request description that explains what changed and why.
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text


def _read_text_with_fallbacks(path: str) -> str:
    encodings_to_try = [
        "utf-8",
        "utf-8-sig",   # handles UTF-8 BOM
        "utf-16",      # auto-detects LE/BE via BOM
        "cp1252",      # common on Windows
        "latin-1",     # last-resort, never fails
    ]
    last_error = None
    for enc in encodings_to_try:
        try:
            with open(path, "r", encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError as e:
            last_error = e
            continue
    if last_error is not None:
        raise last_error
    raise UnicodeDecodeError("unknown", b"", 0, 1, "Unable to decode file with known fallbacks")


def save_pr_description(text: str, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"✅ PR description saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate PR descriptions from a diff file.")
    parser.add_argument("--diff", required=True, help="Path to diff.txt")
    parser.add_argument("--output", required=True, help="Where to save PR_DESCRIPTION.md")
    args = parser.parse_args()

    diff_content = _read_text_with_fallbacks(args.diff)

    print("Generating PR description...")
    pr_description = generate_pr_description(diff_content)
    save_pr_description(pr_description, args.output)


if __name__ == "__main__":
    main()






 