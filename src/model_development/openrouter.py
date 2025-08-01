from openai import OpenAI
from helpers.config import get_settings


def get_sentiment_gemma_14b(prompt: str, api_key: str = None):
<<<<<<< HEAD
    client = OpenAI(
        base_url="https://api.openrouter.ai/v1",
        api_key=get_settings().openrouter_api_key
    )

    response = client.chat.completions.create(
        model=get_settings().openrouter_model,
=======
    # Initialize OpenAI client with OpenRouter API key
    client = OpenAI(
        base_url="https://api.openrouter.ai/v1",
        api_key=get_settings().OPENROUTER_API_KEY
    )

    response = client.chat.completions.create(
        model=get_settings().OPENROUTER_MODEL,
>>>>>>> 3815eccddffd122448034a66c6df5ec620cdbab9
        messages=[
            {"role": "system", "content": "you are a sentiment analysis assistant response with only Positive, Negative or Neutral"},
            {"role": "user", "content": prompt}
        ])
    return response.choices[0].message.content.strip()