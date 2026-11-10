"""Hello LLM: send one prompt to an OpenAI model and print the reply."""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads OPENAI_API_KEY from .env

client = OpenAI()  # picks up OPENAI_API_KEY from the environment

response = client.responses.create(
    model="gpt-4o-mini",
    input="Say hello and tell me one fun fact about large language models.",
)

print(response.output_text)
