
from fastapi import APIRouter
from helpers import get_settings
from helpers import APIStandardFormat   
from transformers import pipeline
from fastapi.responses import JSONResponse
from model_development.openrouter import get_sentiment_gemma_14b
from helpers import SentimentResponse


data_router = APIRouter()

@data_router.post("/get_sentiment")
async def process_data(data: APIStandardFormat):
    settings = get_settings()

    classifier = pipeline(
        "sentiment-analysis",
        model=settings.HUGGING_FACE_MODEL,
        tokenizer=settings.HUGGING_FACE_MODEL
        )
    
    if not data.prompt or len(data.prompt.strip()) == 0:
        return JSONResponse(
            status_code=400,
            content={"error": "Prompt cannot be empty."}
        )
    
    results = classifier(data.prompt)[0]

    return {
        "output": results['label'],
        "score": results['score'],
        }

@data_router.post("/sentiment/openrouter")
async def openrouter_sentiment(data: SentimentResponse):
    if not data.user_text or len(data.user_text.strip()) == 0:
        return JSONResponse(
            status_code=400,
            content={"error": "User text cannot be empty."}
        )
    sentiment = get_sentiment_gemma_14b(data.user_text)
    return {
        "label": sentiment
        }