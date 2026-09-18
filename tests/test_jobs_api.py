from fastapi.testclient import TestClient

from src.api.main import app


client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_search_jobs_endpoint_exists() -> None:
    response = client.get("/jobs/search")

    assert response.status_code == 200
    assert isinstance(response.json(), list)