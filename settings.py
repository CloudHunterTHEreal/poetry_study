from pydantic_settings import BaseSettings
from functools import lru_cache
from loguru import logger


class Settings(BaseSettings):
    # api_version: str = "/api/v1"
    # server_host: str = "0.0.0.0"
    # server_port: int = 5000
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
