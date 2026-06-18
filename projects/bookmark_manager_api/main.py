# I am demonstrating my learning so far in the form of this bookmark manager API project
# bookmark manager api - phase 2
# now uses SQLite database for persistent storage
# added update endpoint, filter by tag, and search by title
# phase 3: will add error handling and tests with pytest

from fastapi import FastAPI, Request
from storage import (
    create_table,
    add_bookmark,
    get_all_bookmarks,
    get_bookmark_by_id,
    update_bookmark,
    delete_bookmark,
    search_bookmarks,
    get_bookmarks_by_tag,
)

app = FastAPI()

# create the table when the app starts
create_table()


@app.get("/bookmarks")
def list_bookmarks(tag: str = None, search: str = None):
    if tag:
        return get_bookmarks_by_tag(tag)
    if search:
        return search_bookmarks(search)
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


@app.put("/bookmarks/{bookmark_id}")
async def edit_bookmark(bookmark_id: int, request: Request):
    data = await request.json()
    bookmark = update_bookmark(bookmark_id, data["title"], data["url"], data.get("tags", []))
    if bookmark is None:
        return {"error": "Bookmark not found"}
    return bookmark


@app.delete("/bookmarks/{bookmark_id}")
def remove_bookmark(bookmark_id: int):
    deleted = delete_bookmark(bookmark_id)
    if deleted:
        return {"message": "Bookmark deleted"}
    return {"error": "Bookmark not found"}
