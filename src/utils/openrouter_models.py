
from openai import OpenAI
from helpers import get_settings


def generate_openrouter_completion(prompt:str):

    # Ensure the OpenRouter API key is set in the environment
    if not get_settings().OPEN_ROUTER_API_KEY:
        raise ValueError("OpenRouter API key is not set in the environment variables.")

        # Create an OpenAI client with the OpenRouter base URL and API key
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=get_settings().OPEN_ROUTER_API_KEY,
    )

    completion = client.chat.completions.create(
    model=get_settings().OPEN_ROUTER_MODEL,
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ]
    )

    return completion.choices[0].message.content
