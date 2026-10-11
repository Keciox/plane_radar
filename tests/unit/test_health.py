from fastapi.testclient import TestClient

from case_opening.main import app

client = TestClient(app)


def test_health_main():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
