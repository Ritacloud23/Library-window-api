from .user import get_user

MAX_ATTEMPTS = 3

login_attempts = {}
locked_users = set()

def login(username, password):
    user = get_user(username)
    if user is None:
        return {
            "success": False,
            "message": "User not found",
        }

    if username in locked_users:
        return {
            "success": False,
            "message": "Account locked",
            
        }

    if user["password"] != password:
        login_attempts[username] = login_attempts.get(username, 0) + 1

        if login_attempts[username] >= MAX_ATTEMPTS:
            locked_users.add(username)
            return {
                "success": False,
                "message": "Account locked after 3 failed attempts",
            }
        return {
            "success": False,
            "message": "Invalid password",
            "attempts": 
        login_attempts[username],
        }

    login_attempts[username] = 0
    return {
            "success": True,
            "username": username,
            "role": user["role"],
        }


def has_permissions(role, action):

    permissions = {
        "chief librarian": {
            "add_book",
            "remove_book",
            "view_book",
            "borrow_book",
            "return_book",
            
        },
        "Member": {
            "view_book",
            "borrow_book",
            "return_book",
        },



    }        

    return action in permissions.get(role, set())

