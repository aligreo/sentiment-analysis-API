
from transformers import pipeline
from dataclasses import dataclass
from helpers.config import settings

@dataclass
class SentimentAnalysis:
    pipeline = pipeline(
        task=settings.task,
        model=settings.model_name,
        tokenizer=settings.model_name
    )

    def analyze(self, text: str):
        results = self.pipeline(text)
        return results[0] if results else None