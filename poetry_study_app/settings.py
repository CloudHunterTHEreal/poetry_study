""" App settings file """
from pydantic import ValidationError
from pydantic_settings import BaseSettings
from loguru import logger


class Settings(BaseSettings):
    """ App settings storage class """
    status_url: str


logger.debug("Try to get settings")
try:
    app_settings = Settings()
except ValidationError as v_ex:
    logger.error(f"{v_ex.errors()}")
    raise v_ex
