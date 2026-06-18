# Bookmark Manager API

REST API for saving and organizing links using FastAPI and SQLite.

## What it does (Phase 2)

- Add a bookmark with title, URL, and optional tags (POST /bookmarks)
- List all bookmarks (GET /bookmarks)
- Get a single bookmark by id (GET /bookmarks/{id})
- Update a bookmark (PUT /bookmarks/{id})
- Delete a bookmark (DELETE /bookmarks/{id})
- Filter bookmarks by tag (GET /bookmarks?tag=python)
- Search bookmarks by title (GET /bookmarks?search=docs)
- Data is stored in a SQLite database so it persists between runs

## Planned for later

- Phase 3: error handling and tests with pytest

## How to run

```
pip install fastapi uvicorn
uvicorn main:app --reload
```

Then open http://localhost:8000/docs to try the API.

## Project structure

- main.py - app setup and API endpoints (orchestrator)
- storage.py - SQLite database functions for all bookmark operations

## Built with

- Python, FastAPI, uvicorn, SQLite
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

### Phase 2
- Connecting to a SQLite database with sqlite3 module
- Creating tables with CREATE TABLE IF NOT EXISTS
- Writing SQL queries for INSERT, SELECT, UPDATE, DELETE
- Using ? placeholders to safely pass values into SQL queries
- Using query parameters in FastAPI for filtering and search
- Using SQL LIKE for keyword search
- Storing lists as comma-separated strings in the database
