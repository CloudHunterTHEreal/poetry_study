""" App settings file """
from functools import lru_cache

from pydantic import ValidationError, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger


class Settings(BaseSettings):
    """ App settings storage class """
    # model_config = SettingsConfigDict(
    #     env_file='.env',
    #     env_file_encoding='utf-8'
    # )
    status_url: str


# @lru_cache
# def get_settings():
#     """ Add .env as environment source file"""
#     appsettings = Settings(
#         _env_file=".env",
#         _env_file_encoding="utf-8"
#     )
#     logger.debug(f"{appsettings = }")
#     return appsettings


logger.debug(f"Try to get settings")
# app_settings = get_settings()
try:
    app_settings = Settings()
except ValidationError as v_ex:
    logger.error(f"{v_ex.errors()}")
    raise v_ex

# app_settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
logger.debug(f"{app_settings = }")
