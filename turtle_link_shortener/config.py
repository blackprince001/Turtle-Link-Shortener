from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        # allows the import of environment variables from .env
        # env file has variables included as attributes in
        # this class and more. you can decide to go with the
        # default preset used above or set your own .env file
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
