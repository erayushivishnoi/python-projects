# storage.py - handles storing and retrieving bookmarks
# for now everything stays in memory, no database yet

bookmarks = []
next_id = 1


def add_bookmark(title, url, tags):
    """add a new bookmark and return it with an id"""
    global next_id
    bookmark = {
        "id": next_id,
        "title": title,
        "url": url,
        "tags": tags,
    }
    bookmarks.append(bookmark)
    next_id = next_id + 1
    return bookmark


def get_all_bookmarks():
    """return all bookmarks"""
    return bookmarks


def get_bookmark_by_id(bookmark_id):
    """find a bookmark by id, return None if not found"""
    for bookmark in bookmarks:
        if bookmark["id"] == bookmark_id:
            return bookmark
    return None


def delete_bookmark(bookmark_id):
    """delete a bookmark by id, return True if deleted, False if not found"""
    for bookmark in bookmarks:
        if bookmark["id"] == bookmark_id:
            bookmarks.remove(bookmark)
            return True
    return False
