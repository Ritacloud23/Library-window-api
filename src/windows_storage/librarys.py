from .books import get_book


def borrow_book(book_id):
    

    book = get_book(book_id)

    if book is None:
        return {
            "success": False,
            "message": "There is no such book",
        }

    if book["status"] == "borrowed":
        return {
            "success": False,
            "message": "Book is already borrowed",
        }

    book["status"] = "borrowed"

    return {
        "success": True,
        "book": book,
        "message": "Book borrowed successfully",
    }


def return_book(book_id):


    book = get_book(book_id)

    if book is None:
        return {
            "success": False,
            "message": "There is no such book",
        }

    if book["status"] == "on shelf":
        return {
            "success": False,
            "message": "Book is already on the shelf",
        }

    book["status"] = "on shelf"

    return {
        "success": True,
        "book": book,
        "message": "Book returned successfully",
    }

