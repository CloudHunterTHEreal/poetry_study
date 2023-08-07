""" App settings file """
from pydantic_core import ValidationError
from pydantic_settings import BaseSettings
from loguru import logger


class Settings(BaseSettings):
    """ App settings storage class """
    status_url: str


logger.info("Example container run command: docker run --name Poetry_Study "
            "--rm -e status_url='/status' -p 8888:8888 <image_ID>")
try:
    app_settings = Settings()
except ValidationError as v_ex:
    logger.error("[!] Project environment variable for '/status' endpoint not found. Add <-e status_url='/status'>")
    logger.error(f"{str(v_ex)}")
    # raise v_ex
