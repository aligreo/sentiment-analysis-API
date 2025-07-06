from pydantic import BaseModel

class APIStandardFormat(BaseModel):
    prompt_id : str
    prompt : str