
from openai import OpenAI
from helpers.config import settings


def generate_response(prompt:str):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.openrouter_api_key,
    )

    completion = client.chat.completions.create(
    model=settings.openrouter_model,
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ]
    )

    return completion.choices[0].message.content
