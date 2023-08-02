from fastapi import FastAPI
from pydantic import BaseModel
from settings import settings


app = FastAPI()


class Status(BaseModel):
    status: str = 'ok'


@app.get(settings.main_url)
def status() -> Status:
    return Status()

"""# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/"""
