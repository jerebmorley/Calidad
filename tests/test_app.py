import pytest
from app import app


@pytest.fixture
def client():
    app.config.update({"TESTING": True})

    with app.test_client() as test_client:
        yield test_client


def test_health_responde_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "service": "calculadora-ci"
    }


def test_inicio_incluye_endpoint_health(client):
    response = client.get("/")
    data = response.get_json()

    assert response.status_code == 200
    assert data["operaciones"]["health"] == "/health"