
from transformers import pipeline
from helpers import get_settings
from dataclasses import dataclass

@dataclass
class SentimentAnalysis:
    def __init__(self):
        model_name: str = get_settings().model_name
        tokenizer_name: str = get_settings().model_name
        self.pipeline = pipeline(
            get_settings().task,
            model=model_name,
            tokenizer=tokenizer_name
        )

    def analyze(self, text: str):
        results = self.pipeline(text)
        return results[0] if results else None