from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def generate_unicorn_story() -> str:
    api_key = os.getenv("KEY")
    client = OpenAI(api_key=api_key)
    
    response = client.responses.create(
        model="gpt-5",
        input="Write a one-sentence bedtime story about a unicorn."
    )
    return response.output_text


def main():
    print("Hello from kreoh-TY-project!")
    story = generate_unicorn_story()
    print(story)


if __name__ == "__main__":
    main()