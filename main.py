from src.windows_storage.auth import login, has_permissions

from src.windows_storage.books import (
    get_book,
    get_books,
    add_book,
    remove_book,
)

from src.windows_storage.librarys import borrow_book, return_book

from src.windows_storage.storage import load_books, save_books


def handle_request(
    method,
    book_id=None,
    username=None,
    password=None,
    title=None,
    author=None,
):
    # User must sign in first
    if not username or not password:
        return {
            "status": 401,
            "message": "Who are you? Sign in first.",
        }

    # Authenticate user
    user = login(username, password)

    if not user["success"]:
        return {
            "status": 401,
            "message": user["message"],
        }

    
    if method == "GET":
        if book_id is not None:
            book = get_book(book_id)

            if book is None:
                return {
                    "status": 404,
                    "message": "There is no such book.",
                }

            return {
                "status": 200,
                "book": book,
            }

        return {
            "status": 200,
            "books": get_books(),
        }

    # POST - Register a new book
    if method == "POST":
        if title is None or author is None:
            return {
                "status": 400,
                "message": "Title and author are required.",
            }

        if not title.strip() or not author.strip():
            return {
                "status": 400,
                "message": "Title and author cannot be empty.",
            }

        book = add_book(title, author)

        save_books(get_books())

        return {
            "status": 200,
            "book": book,
            "message": "Book registered successfully.",
        }

    # PUT - Update a book
    if method == "PUT":
        if book_id is None:
            return {
                "status": 400,
                "message": "Book ID is required.",
            }

        book = get_book(book_id)

        if book is None:
            return {
                "status": 404,
                "message": "There is no such book.",
            }

        if title is not None:
            if not title.strip():
                return {
                    "status": 400,
                    "message": "Title cannot be empty.",
                }

            book["title"] = title

        if author is not None:
            if not author.strip():
                return {
                    "status": 400,
                    "message": "Author cannot be empty.",
                }

            book["author"] = author

        save_books(get_books())

        return {
            "status": 200,
            "book": book,
            "message": "Book updated successfully.",
        }

    # DELETE - Remove a book
    if method == "DELETE":
        if book_id is None:
            return {
                "status": 400,
                "message": "Book ID is required.",
            }

        
        if not has_permissions(user["role"], "remove_book"):
            return {
                "status": 403,
                "message": "You are not allowed to delete books.",
            }

        book = get_book(book_id)

        if book is None:
            return {
                "status": 404,
                "message": "There is no such book.",
            }

        remove_book(book_id)

        save_books(get_books())

        return {
            "status": 200,
            "message": "Book deleted successfully.",
        }

    # BORROW - Borrow a book
    if method == "BORROW":
        if book_id is None:
            return {
                "status": 400,
                "message": "Book ID is required.",
            }

        result = borrow_book(book_id)

        if not result["success"]:
            if result["message"] == "There is no such book":
                return {
                    "status": 404,
                    "message": result["message"],
                }

            return {
                "status": 400,
                "message": result["message"],
            }

        save_books(get_books())

        return {
            "status": 200,
            "book": result["book"],
            "message": result["message"],
        }

    
    if method == "RETURN":
        if book_id is None:
            return {
                "status": 400,
                "message": "Book ID is required.",
            }

        result = return_book(book_id)

        if not result["success"]:
            if result["message"] == "There is no such book":
                return {
                    "status": 404,
                    "message": result["message"],
                }

            return {
                "status": 400,
                "message": result["message"],
            }

        save_books(get_books())

        return {
            "status": 200,
            "book": result["book"],
            "message": result["message"],
        }

    # Unknown request
    return {
        "status": 400,
        "message": "Invalid request.",
    }


