from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_projects():
    response = client.get("/api/projects")
    assert response.status_code == 200
    assert response.json()["count"] == 2


def test_missing_project():
    assert client.get("/api/projects/missing").status_code == 404


def test_contact_validation():
    response = client.post("/api/contact", json={
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "message": "Please contact me about a project.",
    })
    assert response.status_code == 200
    assert response.json()["accepted"] is True


def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    assert "Augustine Isama" in response.text
