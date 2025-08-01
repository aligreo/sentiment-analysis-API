from openai import OpenAI
from helpers.config import get_settings


def get_sentiment_gemma_14b(prompt: str, api_key: str = None):
    client = OpenAI(
        base_url="https://api.openrouter.ai/v1",
        api_key=get_settings().openrouter_api_key
    )

    response = client.chat.completions.create(
        model=get_settings().openrouter_model,
        messages=[
            {"role": "system", "content": "you are a sentiment analysis assistant response with only Positive, Negative or Neutral"},
            {"role": "user", "content": prompt}
        ])
    return response.choices[0].message.content.strip()