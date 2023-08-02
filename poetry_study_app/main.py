""" Main module """
from fastapi import FastAPI
from pydantic import BaseModel
from .settings import app_settings


app = FastAPI()


class Status(BaseModel):
    """ App status class """
    status: str = 'ok'


@app.get(app_settings.status_url)
def status() -> Status:
    """ Status request func """
    return Status()
