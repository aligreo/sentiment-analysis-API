
from transformers import pipeline
from dataclasses import dataclass

@dataclass
class SentimentAnalysis:
    task: str = "sentiment-analysis"
    model_name: str = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer_name : str = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    pipeline = pipeline(
        task=task,
        model=model_name,
        tokenizer=tokenizer_name
    )

    def analyze(self, text: str):
        results = self.pipeline(text)
        return results[0] if results else None