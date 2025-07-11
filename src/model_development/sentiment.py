
from transformers import pipeline
from helpers import get_settings

class SentimentAnalysis:
    def __init__(self):
        self.model_name = get_settings().TRAINED_MODEL_PATH
        self.tokenizer_name = get_settings().TRAINED_MODEL_PATH
        self.pipeline = pipeline(
            "sentiment-analysis",
            model=self.model_name,
            tokenizer=self.tokenizer_name
        )

    def analyze(self, text: str):
        results = self.pipeline(text)
        return results[0] if results else None