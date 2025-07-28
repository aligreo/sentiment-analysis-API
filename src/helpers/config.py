
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    HUGGING_FACE_API_KEY: str 
    HUGGING_FACE_MODEL:str
    HUGGING_FACE_TASK : str
    DATA_BASE_URI : str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

def get_settings() -> Settings:
    return Settings()