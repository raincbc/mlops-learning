def is_valid_user_profile(data):
    if not isinstance(data, dict):
        return False

    user_id = data.get("id")
    if not isinstance(user_id, int):
        return False

    profile = data.get("profile")
    if not isinstance(profile, dict):
        return False

    name = profile.get("name")
    if not isinstance(name, str) or name.strip() == "":
        return False

    email = profile.get("email")
    if not isinstance(email, str) or "@" not in email:
        return False

    age = profile.get("age")
    if not isinstance(age, int) or not (0 <= age <= 120):
        return False

    return True
