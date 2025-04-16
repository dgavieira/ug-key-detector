from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # FastAPI
    app_name: str = "UG Key Detector (RAG)"
    # HTTP
    user_agent: str = "ug-key-detector/0.1 (https://github.com/yourname)"
    timeout_s: int = 10
    # LLM / OpenAI
    openai_api_key: str | None = None  # read from env
    model_config = SettingsConfigDict(env_file=".env", env_prefix="KEYDET_")

@lru_cache
def get_settings() -> Settings:
    return Settings()
