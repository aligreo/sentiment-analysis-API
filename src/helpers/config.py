
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str
    app_version: str
    app_description: str
    hugging_face_api_key: str 
    hugging_face_model:str
    hugging_face_task: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

def get_settings() -> Settings:
    return Settings()