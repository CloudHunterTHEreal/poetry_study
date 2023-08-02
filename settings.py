from pydantic_settings import BaseSettings
from functools import lru_cache
from loguru import logger


class Settings(BaseSettings):
    status_url: str


@lru_cache
def get_settings():
    appsettings = Settings(
        _env_file=".env",
        _env_file_encoding="utf-8"
    )
    return appsettings


app_settings = get_settings()
logger.debug(f"{app_settings = }")
