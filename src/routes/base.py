from fastapi import FastAPI
from fastapi import APIRouter

from helpers import get_settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api"],
)   

@base_router.get("/")
async def read_root():
    """
    Root endpoint to check if the API is running.
    """
    settings = get_settings()
    return {
        "message": "Welcome to the Sentiment Analysis API",
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        "app_description": settings.app_description,
        "hugging_face_model": settings.hugging_face_model,
        "hugging_face_task": settings.hugging_face_task,
    }