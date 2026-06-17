# I am demonstrating my learning so far in the form of this bookmark manager API project
# bookmark manager api - phase 1
# basic REST API with in-memory storage
# I have planned this in 2 more phases
# phase 2: replace in-memory list with SQLite database, add update endpoint, filtering and search
# phase 3: will add error handling and tests with pytest

from fastapi import FastAPI, Request
from storage import add_bookmark, get_all_bookmarks, get_bookmark_by_id, delete_bookmark

app = FastAPI()


@app.get("/bookmarks")
def list_bookmarks():
    return get_all_bookmarks()


@app.get("/bookmarks/{bookmark_id}")
def get_bookmark(bookmark_id: int):
    bookmark = get_bookmark_by_id(bookmark_id)
    if bookmark is None:
        return {"error": "Bookmark not found"}
    return bookmark


@app.post("/bookmarks")
async def create_bookmark(request: Request):
    data = await request.json()
    bookmark = add_bookmark(data["title"], data["url"], data.get("tags", []))
    return bookmark


@app.delete("/bookmarks/{bookmark_id}")
def remove_bookmark(bookmark_id: int):
    deleted = delete_bookmark(bookmark_id)
    if deleted:
        return {"message": "Bookmark deleted"}
    return {"error": "Bookmark not found"}
