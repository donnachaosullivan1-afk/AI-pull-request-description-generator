from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


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
    story = generate_pr_description(client)
    print(story)



if __name__ == "__main__":
    main() 




