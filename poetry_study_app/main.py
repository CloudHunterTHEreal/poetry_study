""" Main module """
from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger
from poetry_study_app.settings import app_settings


app = FastAPI()


class Status(BaseModel):
    """ App status class """
    status: str = 'ok'


@app.get(app_settings.status_url, tags=['Example routers'])
async def status() -> Status:
    """ Status request func """
    logger.debug(f"{app_settings.status_url = }")
    return Status()
