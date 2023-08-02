from fastapi.testclient import TestClient
from main import app
from settings import app_settings


def test_inside_run():
    client = TestClient(app)
    result = client.get(app_settings.status_url)

    assert result.status_code == 200
    assert result.json() == {'status': 'ok'}
