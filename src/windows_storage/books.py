from . import storage

def get_all(status_filter=None):
    books = storage.load_books()
    if status_filter:
        return [book for book in books if book['status'] == status_filter]
    return books

def get_one(book_id):
    books = storage.load_books()
    for b in books:
        if b['id'] == book_id:
            return b
    return None

def create(title, author):
    books = storage.load_books()
    new_id = max((b["id"] for b in books), default=0) + 1
    new_book = {"id": new_id, "title": title, "author": author, "status": "on shell"}
    books.append(new_book)
    storage.save_books(books)
    return new_book

def update(book_id, title=None, author=None):
    books = storage.load_books()
    for b in books:
        if b['id'] == book_id:
            if title is not None:
                b['title'] = title
            if author is not None:
                b['author'] = author
            storage.save_books(books)
            return b
    return None

def delete(book_id):
    books = storage.load_books()
    for i, b in enumerate(books):
        if b['id'] == book_id:
            remove = books.pop(i)
            storage.save_books(books)
            return remove
    return None