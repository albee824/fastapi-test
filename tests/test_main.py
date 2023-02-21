from fastapi.testclient import TestClient
import sys
sys.path.append('../')

from api.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_calc_double_2_success():
    response = client.get("/calc/double/2")
    assert response.status_code == 200
    assert response.json() == {"num": 2, "answer": 4}

def test_calc_double_4_success():
    response = client.get("/calc/double/4")
    assert response.status_code == 200
    assert response.json() == {"num": 4, "answer": 8}
