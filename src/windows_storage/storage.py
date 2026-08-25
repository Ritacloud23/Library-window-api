import json
import os
from pathlib import Path


DATA_DIR = Path(__file__).parent / "data"
BOOKS_PATH = DATA_DIR / "books.json"
AUTHORS_PATH = DATA_DIR / "authors.json"

def get_authors():
    return [
        "Chinua Achebe",
        "Chimamanda Adichie",
        "Ben Okri",
        "Ken Saro-Wiwa",
        "Cyprian Ekwensi",
        "Buchi Emecheta",
        "Chinua Achebe",
        "Ayobami Adebayo",
        "Chigozie Obioma",
        "Chimamanda Adichie",
    ]



def get_books():
    return [
        "things fall apart",
        "the hitchhiker's guide to the galaxy",
        "the dark side of the moon",
        "the wind from the sea",
        "a fire upon the deep",
        "the last of us",
        "a fire upon the deep",
        "the last of us",
        "the hitchhiker's guide to the galaxy",
        "the dark side of the moon",
        "the wind from the sea",
        "books of the world",
        "a fire upon the deep",
        "book of the dead",
        "book of the dead",
    ]

def _ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def _load_list(path, seed, save_fn):
    _ensure_data_dir()
    if not path.exists():
        save_fn(seed)
        return list(seed)

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("books file did not contain a list")
        return data
    except (json.JSONDecodeError, ValueError, OSError):
        try:
            os.replace(path, path.with_suffix(".corrupted.json"))
        except OSError:
            pass
        save_fn(seed)
        return list(seed)


def _save_list(path, items):
    _ensure_data_dir()    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)

def _load_books(items):
    _save_list(BOOKS_PATH, items)

def save_books():
    return _load_list(BOOKS_PATH, get_books, save_books)


def  save_books(books):
    _save_list(BOOKS_PATH, books)   


def load_authors():
    return _load_list(AUTHORS_PATH, get_authors, save_authors)


def save_authors(authors):
    _save_list(AUTHORS_PATH, authors)