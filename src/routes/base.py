
from fastapi import FastAPI, Request
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.responses import JSONResponse
from helpers import get_settings
from model_development import SentimentAnalysis

template = Jinja2Templates(directory="templates")

base_router = APIRouter()   

@base_router.get("/")
async def main(request: Request):

    settings = get_settings()

    return template.TemplateResponse(
        request=request,
        name = "index.html"
        )

@base_router.post("/")
async def get_user_data(request:Request, user_text :str = Form(...)):
    if isinstance(user_text, str) and len(user_text) > 0:
        sentiment = SentimentAnalysis().analyze(user_text)
        if sentiment['label'] == 'LABEL_0':
            sentiment['label'] = 'Negative'
        else:
            sentiment['label'] = 'Positive'

        return template.TemplateResponse(
            request = request,
            name="index.html",
            context = {
                'request':request,
                "sentiment": sentiment['label'],
                "score": round(sentiment['score'], 2),
            }
        )
        
    return JSONResponse(
        status_code=404,
        content = {"message":"Please provide a valid text input."}
    )

        


