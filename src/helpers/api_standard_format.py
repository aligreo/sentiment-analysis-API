from pydantic import BaseModel

class APIStandardFormat(BaseModel):
    text_id : str
    text : str