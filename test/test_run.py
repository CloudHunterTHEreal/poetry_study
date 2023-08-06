from fastapi.testclient import TestClient
from poetry_study_app.main import app
from poetry_study_app.settings import app_settings


def test_inside_run() -> None:
    client = TestClient(app)
    request_path = app_settings.status_url
    result = client.get(request_path)

    assert result.status_code == 200
    assert result.json() == {'status': 'ok'}
