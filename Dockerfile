FROM python:3.11.2-alpine

EXPOSE 8888

WORKDIR /code

RUN pip install --upgrade pip
RUN apk add gcc musl-dev libffi-dev
RUN pip install poetry

COPY . /code

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --without test

CMD ["poetry", "run", "uvicorn", "poetry_study_app.main:app", "--host", "0.0.0.0", "--port", "8888"]