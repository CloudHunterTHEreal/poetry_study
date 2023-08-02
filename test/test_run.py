from fastapi.testclient import TestClient
from poetry_study_app.main import app
from poetry_study_app.settings import app_settings


def test_inside_run():
    client = TestClient(app)
    result = client.get(app_settings.status_url)

    assert result.status_code == 200
    assert result.json() == {'status': 'ok'}
