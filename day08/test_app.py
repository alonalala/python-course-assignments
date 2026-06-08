from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "documentation" in response.json()["message"]

def test_analyze_endpoint_success():
    payload = {
        "sequence": "ATGCGTGCGAGCGCATGCAT",
        "window_size": 10
    }
    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["sequence_length"] == 20
    assert len(data["profile"]) > 0