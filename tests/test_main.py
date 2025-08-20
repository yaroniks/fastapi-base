from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_home():
    response = client.get('/')
    assert response.status_code == 200


def test_example():
    response = client.get('/example')
    data = response.json()
    assert data['success'] is True
