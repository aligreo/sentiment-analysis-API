from fastapi import FastAPI, Request
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.responses import JSONResponse, RedirectResponse
# from helpers import get_settings
from model_development.sentiment import SentimentAnalysis
from models import Texts, sessionLocal


template = Jinja2Templates(directory="templates")
app = FastAPI()   

@app.get("/")
async def main(request: Request):
    # settings = get_settings()
    return template.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "app_name":"Sentiment Analysis API",
            "app_version": "1.0",
        }
    )

@app.post("/")
async def get_user_data(request: Request, user_text: str = Form(...)):
    if isinstance(user_text, str) and len(user_text.strip()) > 0:
        sentiment = SentimentAnalysis().analyze(user_text)
        label = sentiment.get('label', 'Unknown')
        score = sentiment.get('score', 0.0)

        db = sessionLocal()
        observation = Texts(text=user_text, label=label, score=score)
        db.add(observation)
        db.commit()
        db.refresh(observation)
        db.close()

        return template.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "request": request,
                "sentiment": label,
                "score": score
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