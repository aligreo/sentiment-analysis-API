from fastapi import FastAPI, Request
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from helpers import get_settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api"],
)   

@base_router.get("/")
async def main(request: Request):

    settings = get_settings()

    template = Jinja2Templates(directory="templates")
    return template.TemplateResponse(
        request=request,
        name = "index.html",
        context={
            "app_name": settings.APP_NAME,
            "app_version": settings.APP_VERSION,
            "app_descripton": settings.APP_DESCRIPTION
        })