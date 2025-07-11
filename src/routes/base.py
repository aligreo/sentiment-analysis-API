from fastapi import FastAPI, Request
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.responses import JSONResponse, RedirectResponse
from helpers import get_settings
from model_development import SentimentAnalysis

template = Jinja2Templates(directory="templates")

base_router = APIRouter()   

@base_router.get("/")
async def main(request: Request):
    settings = get_settings()
    return template.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "sentiment": None,
            "score": None,
            "app_name": getattr(settings, "app_name", "Sentiment Analysis"),
            "app_version": getattr(settings, "app_version", "1.0"),
            "app_description": getattr(settings, "app_description", "Analyze the sentiment of your text!"),
        }
    )

@base_router.post("/")
async def get_user_data(request: Request, user_text: str = Form(...)):
    if isinstance(user_text, str) and len(user_text.strip()) > 0:
        sentiment = SentimentAnalysis().analyze(user_text)
        return template.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "request": request,
                "sentiment": sentiment.get('label', 'Unknown'),
                "score": sentiment.get('score', 0.0),
                "user_text": user_text,
            }
        )
    return template.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "sentiment": None,
            "score": None,
            "error": "Please provide a valid text input.",
        },
        status_code=400
    )




