from fastapi import FastAPI, Request
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.responses import JSONResponse, RedirectResponse
from markdown import markdown
# from helpers import get_settings
from LLM.sentiment import SentimentAnalysis
from models import Texts, sessionLocal
from helpers.config import settings
from LLM.openrouter import generate_response

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

@app.get("/history")
async def get_history(request: Request):
    return template.TemplateResponse(
        request=request,
        name="history.html",
        context={
            "app_name": settings.app_name,
            "app_version": settings.app_version,
            "description": settings.app_description,
        }
    )


@app.get("/generate")
def generate(request: Request):
    return template.TemplateResponse(
        request=request,
        name  ="generate.html",
        context={"request": request}
    )
@app.post("/generate")
def generate(request: Request, prompt: str=Form(...)):
    response = generate_response(prompt)
    html_response = markdown(response) if response else ""
    return template.TemplateResponse(
        request=request,
        name  ="generate.html",
        context={
            "response": html_response
        })


