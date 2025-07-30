
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

    class Config:
        env_file = ".env"

settings = Settings()