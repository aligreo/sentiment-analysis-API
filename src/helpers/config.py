
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    app_version: str
    app_description: str
    hugging_face_api_key: str 
    hugging_face_model:str
    hugging_face_task: str
    SYSTEM_PROMPT : str
    OPEN_ROUTER_API_KEY: str
    OPEN_ROUTER_MODEL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

def get_settings() -> Settings:
    return Settings()