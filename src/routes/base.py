from fastapi import FastAPI
from fastapi import APIRouter

from helpers import get_settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api"],
)   

@base_router.get("/")
async def read_root():
    settings = get_settings()
    return {
        "message": "Welcome to the Sentiment Analysis API",
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        "app_description": settings.app_description,
    }