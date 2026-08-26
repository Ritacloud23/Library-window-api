import json
from pathlib import Path

from .books import BOOKS


DATA_DIR = Path("data")
BOOKS_FILE = DATA_DIR / "books.json"


def save_books(books):
    

    DATA_DIR.mkdir(exist_ok=True)

    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)


def load_books():
    if not BOOKS_FILE.exists():
        save_books(BOOKS)
        return BOOKS

    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            books = json.load(file)

        if not isinstance(books, list):
            print("Saved ledger is invalid. Starting with the default books.")
            save_books(BOOKS)
            return BOOKS

        return books

    except (json.JSONDecodeError, OSError):
        print("Saved ledger could not be read. Starting with the default books.")
        save_books(BOOKS)
        return BOOKS


