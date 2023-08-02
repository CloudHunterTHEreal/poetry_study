from pydantic_settings import BaseSettings
from loguru import logger


class Settings(BaseSettings):
    main_url: str = '/status'


logger.debug(f"Predef {Settings() =}")

settings = Settings()

logger.debug(f"Postdef {Settings() =}")
