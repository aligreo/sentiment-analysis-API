
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
<<<<<<< HEAD
    app_name : str
    app_version : str
    app_description : str
    task : str
    model_name : str
    hf_api_key : str
    database_url : str
    table_name : str
    openrouter_api_key : str
    openrouter_model : str
=======
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    HUGGING_FACE_API_KEY: str 
    HUGGING_FACE_MODEL:str
    HUGGING_FACE_TASK : str
    DATA_BASE_URI : str
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL: str
>>>>>>> 3815eccddffd122448034a66c6df5ec620cdbab9

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

def get_settings() -> Settings:
    return Settings()