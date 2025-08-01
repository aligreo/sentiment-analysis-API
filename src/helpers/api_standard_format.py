
from pydantic import BaseModel

class APIStandardFormat(BaseModel):
    prompt : str

class SentimentResponse(BaseModel):
    user_text: str
    