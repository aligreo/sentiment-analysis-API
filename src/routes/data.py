
from fastapi import APIRouter
from helpers import get_settings
from helpers import APIStandardFormat   
from utils import LoadModel
from datetime import datetime
from utils.openrouter_models import generate_openrouter_completion
from utils.qwen import generate_with_qwen


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api","data"],
)

@data_router.post("/process")
async def process_data(data: APIStandardFormat):
    settings = get_settings()

    generated_output = generate_openrouter_completion(prompt=data.prompt)
    return {
        "time": datetime.now(),
        "output": generated_output
    }