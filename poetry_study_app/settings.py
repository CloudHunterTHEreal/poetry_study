""" App settings file """
from pydantic import ValidationError
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
    logger.error("[!] Project environment variable for '/status' endpoint not found\n"
                 "[!] add -e status_url='/status' into docker run string/")
    raise v_ex
