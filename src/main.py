#!/usr/bin/env python3

import argparse
import subprocess
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
api_key = os.getenv("KEY")
client = OpenAI(api_key=api_key)

def get_diff(diff_path):
    """Return the diff text. If no diff file is provided, generate one using git diff."""
    
    # If user provided a diff file and it exists, use it.
    if diff_path and os.path.exists(diff_path):
        with open(diff_path, "r") as f:
            return f.read()

    # Otherwise, auto-generate diff from git
    print("No diff file provided. Auto-generating diff from Git...")
    diff = subprocess.check_output(["git", "diff"]).decode("utf-8")

    # Ensure input/ directory exists
    os.makedirs("input", exist_ok=True)

    # Save auto-generated diff
    auto_diff_path = "input/diff.txt"
    with open(auto_diff_path, "w") as f:
        f.write(diff)

    print(f"Generated diff saved to {auto_diff_path}")
    return diff


def generate_pr_description(diff):
    """Send diff to OpenAI model to generate PR description."""
    print("Generating PR description...")

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "You are an AI that writes high quality PR descriptions."},
            {"role": "user", "content": diff}
        ]
    )

    return response.choices[0].message.content.strip()


def save_pr_description(pr_text, output_path):
    """Save PR description to output file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(pr_text)
    print(f"✅ PR description saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate a PR description from code changes.")
    parser.add_argument("--diff", type=str, help="Path to diff file (optional). If omitted, git diff is used.")
    parser.add_argument("--output", type=str, required=True, help="Where to save PR description.")
    args = parser.parse_args()

    diff = get_diff(args.diff)
    pr_description = generate_pr_description(diff)
    save_pr_description(pr_description, args.output)


if __name__ == "__main__":
    main()






 