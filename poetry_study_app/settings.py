""" App settings file """
from functools import lru_cache
from pydantic_settings import BaseSettings
from loguru import logger


class Settings(BaseSettings):
    """ App settings storage class """
    status_url: str


# @lru_cache
# def get_settings():
#     """ Add .env as environment source file"""
#     appsettings = Settings(
#         _env_file="poetry_study_app/.env",
#         _env_file_encoding="utf-8"
#     )
#     return appsettings
#
#
# app_settings = get_settings()

app_settings = Settings()
logger.debug(f"{app_settings = }")
