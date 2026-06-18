# storage.py - handles storing and retrieving bookmarks
# now uses SQLite database instead of an in-memory list
# tags are stored as a comma-separated string in the database

import sqlite3

DB_FILE = "bookmarks.db"


def get_connection():
    """connect to the database"""
    conn = sqlite3.connect(DB_FILE)
    return conn


def create_table():
    """create the bookmarks table if it doesn't exist"""
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            tags TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_bookmark(title, url, tags):
    """add a new bookmark and return it"""
    tags_str = ",".join(tags)
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO bookmarks (title, url, tags) VALUES (?, ?, ?)",
        (title, url, tags_str),
    )
    bookmark_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"id": bookmark_id, "title": title, "url": url, "tags": tags}


def get_all_bookmarks():
    """return all bookmarks"""
    conn = get_connection()
    rows = conn.execute("SELECT id, title, url, tags FROM bookmarks").fetchall()
    conn.close()
    bookmarks = []
    for row in rows:
        tags = row[3].split(",") if row[3] else []
        bookmarks.append({"id": row[0], "title": row[1], "url": row[2], "tags": tags})
    return bookmarks


def get_bookmark_by_id(bookmark_id):
    """find a bookmark by id, return None if not found"""
    conn = get_connection()
    row = conn.execute(
        "SELECT id, title, url, tags FROM bookmarks WHERE id = ?",
        (bookmark_id,),
    ).fetchone()
    conn.close()
    if row is None:
        return None
    tags = row[3].split(",") if row[3] else []
    return {"id": row[0], "title": row[1], "url": row[2], "tags": tags}


def update_bookmark(bookmark_id, title, url, tags):
    """update a bookmark by id, return the updated bookmark or None if not found"""
    conn = get_connection()
    tags_str = ",".join(tags)
    cursor = conn.execute(
        "UPDATE bookmarks SET title = ?, url = ?, tags = ? WHERE id = ?",
        (title, url, tags_str, bookmark_id),
    )
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        return None
    return {"id": bookmark_id, "title": title, "url": url, "tags": tags}


def delete_bookmark(bookmark_id):
    """delete a bookmark by id, return True if deleted, False if not found"""
    conn = get_connection()
    cursor = conn.execute("DELETE FROM bookmarks WHERE id = ?", (bookmark_id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0


def search_bookmarks(keyword):
    """search bookmarks by title"""
    conn = get_connection()
    rows = conn.execute(
        "SELECT id, title, url, tags FROM bookmarks WHERE title LIKE ?",
        (f"%{keyword}%",),
    ).fetchall()
    conn.close()
    bookmarks = []
    for row in rows:
        tags = row[3].split(",") if row[3] else []
        bookmarks.append({"id": row[0], "title": row[1], "url": row[2], "tags": tags})
    return bookmarks


def get_bookmarks_by_tag(tag):
    """get all bookmarks that have a specific tag"""
    conn = get_connection()
    rows = conn.execute("SELECT id, title, url, tags FROM bookmarks").fetchall()
    conn.close()
    bookmarks = []
    for row in rows:
        tags = row[3].split(",") if row[3] else []
        if tag in tags:
            bookmarks.append({"id": row[0], "title": row[1], "url": row[2], "tags": tags})
    return bookmarks
