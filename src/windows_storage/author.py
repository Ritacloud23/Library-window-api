from . import storage

def get_all():
    return storage.load_authors()

def get_one(author_id):
    for a in storage.load_authors():
        if a['id'] == author_id:
            return a
    return None