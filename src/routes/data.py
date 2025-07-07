
from fastapi import APIRouter
from helpers import get_settings
from helpers import APIStandardFormat   
from transformers import pipeline
from fastapi.responses import JSONResponse


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api","data"],
)

@data_router.post("/get_sentiment")
async def process_data(data: APIStandardFormat):
    settings = get_settings()

    classifier = pipeline(
        "sentiment-analysis",
        model=settings.TRAINED_MODEL_PATH,
        tokenizer=settings.TRAINED_MODEL_PATH
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