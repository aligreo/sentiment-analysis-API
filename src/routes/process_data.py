
from fastapi import APIRouter
from helpers import get_settings

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api","data"],
)

@data_router.post("/process")
async def process_data(data: dict):
    settings = get_settings()
    
    pass