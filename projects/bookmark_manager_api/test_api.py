# test_api.py - tests for the bookmark manager API using pytest
# uses FastAPI's TestClient to send requests without starting a real server
# each test uses a fresh database so tests don't affect each other

import os
import pytest
from fastapi.testclient import TestClient

# use a test database instead of the real one
import storage
storage.DB_FILE = "test_bookmarks.db"

from main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_database():
    """delete the test database before and after each test"""
    if os.path.exists("test_bookmarks.db"):
        os.remove("test_bookmarks.db")
    storage.create_table()
    yield
    if os.path.exists("test_bookmarks.db"):
        os.remove("test_bookmarks.db")


def test_add_bookmark():
    response = client.post("/bookmarks", json={"title": "Google", "url": "https://google.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Google"
    assert data["url"] == "https://google.com"
    assert data["tags"] == []


def test_add_bookmark_with_tags():
    response = client.post("/bookmarks", json={"title": "Python", "url": "https://python.org", "tags": ["python"]})
    assert response.status_code == 200
    assert response.json()["tags"] == ["python"]


def test_add_bookmark_missing_title():
    response = client.post("/bookmarks", json={"url": "https://google.com"})
    assert response.status_code == 400


def test_add_bookmark_missing_url():
    response = client.post("/bookmarks", json={"title": "Google"})
    assert response.status_code == 400


def test_list_bookmarks():
    client.post("/bookmarks", json={"title": "Google", "url": "https://google.com"})
    client.post("/bookmarks", json={"title": "Python", "url": "https://python.org"})
    response = client.get("/bookmarks")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_bookmark_by_id():
    client.post("/bookmarks", json={"title": "Google", "url": "https://google.com"})
    response = client.get("/bookmarks/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Google"


def test_get_bookmark_not_found():
    response = client.get("/bookmarks/99")
    assert response.status_code == 404


def test_update_bookmark():
    client.post("/bookmarks", json={"title": "Google", "url": "https://google.com"})
    response = client.put("/bookmarks/1", json={"title": "Google Search", "url": "https://google.com", "tags": ["search"]})
    assert response.status_code == 200
    assert response.json()["title"] == "Google Search"
    assert response.json()["tags"] == ["search"]


def test_update_bookmark_not_found():
    response = client.put("/bookmarks/99", json={"title": "X", "url": "https://x.com"})
    assert response.status_code == 404


def test_update_bookmark_missing_fields():
    client.post("/bookmarks", json={"title": "Google", "url": "https://google.com"})
    response = client.put("/bookmarks/1", json={"title": "Google"})
    assert response.status_code == 400


def test_delete_bookmark():
    client.post("/bookmarks", json={"title": "Google", "url": "https://google.com"})
    response = client.delete("/bookmarks/1")
    assert response.status_code == 200
    # confirm it's gone
    response = client.get("/bookmarks/1")
    assert response.status_code == 404


def test_delete_bookmark_not_found():
    response = client.delete("/bookmarks/99")
    assert response.status_code == 404


def test_filter_by_tag():
    client.post("/bookmarks", json={"title": "Python", "url": "https://python.org", "tags": ["python", "docs"]})
    client.post("/bookmarks", json={"title": "Google", "url": "https://google.com", "tags": ["search"]})
    response = client.get("/bookmarks?tag=python")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Python"


def test_search_by_title():
    client.post("/bookmarks", json={"title": "Python Docs", "url": "https://python.org"})
    client.post("/bookmarks", json={"title": "Google", "url": "https://google.com"})
    response = client.get("/bookmarks?search=Python")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Python Docs"
