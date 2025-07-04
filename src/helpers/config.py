
from pydantic import BaseSettings, Field
from typing import Optional

class Settings(BaseSettings):
    app_name: str = Field(..., env="APP_NAME")
    app_version: str = Field(..., env="APP_VERSION")
    app_description: str = Field(..., env="APP_DESCRIPTION")
    hugging_face_api_key: Optional[str] = Field(None, env="HUGGING_FACE_API_KEY")
    hugging_face_model: Optional[str] = Field(None, env="HUGGING_FACE_MODEL")
    hugging_face_task: Optional[str] = Field(None, env="HUGGING_FACE_TASK")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"