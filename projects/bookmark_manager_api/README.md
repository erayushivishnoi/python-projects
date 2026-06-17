# Bookmark Manager API

REST API for saving and organizing links using FastAPI and SQLite.

## What it does (Phase 1)

- Add a bookmark with title, URL, and optional tags (POST /bookmarks)
- List all bookmarks (GET /bookmarks)
- Get a single bookmark by id (GET /bookmarks/{id})
- Delete a bookmark (DELETE /bookmarks/{id})
- Data stays in memory for now, no database yet

## Planned for later

- Phase 2: SQLite database, update endpoint, filter by tag, search by title
- Phase 3: error handling and tests with pytest

## How to run

```
pip install fastapi uvicorn
uvicorn main:app --reload
```

Then open http://localhost:8000/docs to try the API.

## Project structure

- main.py - app setup and API endpoints (orchestrator)
- storage.py - in-memory list and functions to add/get/delete bookmarks

## Built with

- Python, FastAPI, uvicorn
- Split across two files instead of one big main.py

## What I learned building this

### Phase 1
- Setting up a FastAPI app and defining API endpoints
- Using HTTP methods (GET, POST, DELETE) for different operations
- Reading JSON from a request body using Request
- Splitting code into separate files (main, storage)
- Importing functions from other files
- Using async/await for the first time
- Using .get() on a dictionary to provide a default value
