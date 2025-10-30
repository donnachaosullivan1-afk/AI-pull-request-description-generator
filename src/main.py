from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
def save_pr_description(pr_text: str):
    with open("output/PR_DESCRIPTION.md", "w") as f:
        f.write(pr_text)

def generate_pr_description(client: OpenAI) -> str:
    with open("input/diff.txt", "r") as f:
        diff = f.read()

    prompt = f"""
        "You are a helpful assistant that generates PR descriptions."
        "# comment to LLM
        "# the text below is the diff of code changes. summarise what changed and why.
        {diff}
        "please write a clear and professional PR description in markdown format."""
    
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )
    return response.output_text


def main():
    api_key = os.getenv("KEY")
    client = OpenAI(api_key=api_key)
    pr_description = generate_pr_description(client)
    print(pr_description)
    save_pr_description(pr_description)


if __name__ == "__main__":
    main() 




