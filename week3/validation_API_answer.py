users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie", "email": None}
]

def is_valid_user_list(data):
    if len(data) == 0:
        return False
    for user in data:
        if not user.get("id") or not isinstance(user.get("id"), int):
            return False
        if not user.get("name") or not isinstance(user.get("name"), str):
            return False
        email = user.get("email")
        if email is not None:
            if not isinstance(email, str) or "@" not in email:
                return False
    return True
print(is_valid_user_list(users))