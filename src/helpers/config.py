
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    hugging_face_api_key: str 
    hugging_face_model:str
    hugging_face_task: str
    OPEN_ROUTER_API_KEY: str
    OPEN_ROUTER_MODEL: str
    TRAINED_MODEL_PATH: str
    DATA_BASE_URI : str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

def get_settings() -> Settings:
    return Settings()