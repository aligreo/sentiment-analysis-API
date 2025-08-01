
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
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

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

def get_settings() -> Settings:
    return Settings()