
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_petrol_price(client):
    response = client.get("/price/petrol")

    assert response.status_code == 200
    assert response.get_json() == {
        "fuel": "petrol",
        "price": 95.5
    }


def test_diesel_price(client):
    response = client.get("/price/diesel")

    assert response.status_code == 200
    assert response.get_json() == {
        "fuel": "diesel",
        "price": 88.2
    }


def test_unknown_fuel(client):
    response = client.get("/price/unknown")

    assert response.status_code == 404
    assert response.get_json() == {
        "error": "unknown fuel"
    }

