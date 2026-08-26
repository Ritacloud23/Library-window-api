USERS = {
    "mrs_okafor": {"password": "library2024", "role": "chief librarian"},
    "bello": {"password": "windowboy", "role": "member"},
    "amina_s": {"password": "Amina3425", "role": "member"},
    "chinyere": {"password": "booklife", "role": "member"},
    "rita": {"password": "rita123", "role": "member"},
    "chidimma": {"password": "chidimma123", "role": "member"},
}


def get_user(username):
    return USERS.get(username)


def user_exists(username):
    return username in USERS


