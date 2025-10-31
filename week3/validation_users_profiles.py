users = [
    {
        "id": 1,
        "name": "Alice",
        "profile": {
            "age": 30,
            "gender": "female"
        },
        "address": {
            "city": "Kyiv",
            "zip": "01001"
        },
        "interests": ["reading", "travel"],
        "email": "alice@example.com"
    },
]

def is_valid_user_list(data):
    for user in data:
        if not "id" in user:
            return False
        if not isinstance(user.get("id"), int) or user.get("id") <= 0:
            return False
        if  not "name" in user:
            return False
        if not isinstance(user.get("name"), str) or len(user.get("name")) == 0:
            return False
        if not "profile" in user or not isinstance(user.get("profile"), dict):
            return False
        if not "age" in user.get("profile") or not "gender" in user.get("profile"):
            return False
        if not isinstance(user.get("profile").get("age"), int) or not isinstance(user.get("profile").get("gender"), str):
            return False
#---------------Cокращение---------------------------------------------------
        profile = user.get("profile")
        if not isinstance(profile, dict):
            return False
        if not isinstance(profile.get("age"), int) or not isinstance(profile.get("gender"), str):
            return False
#-----------------------------------------------------------------------------------------
        address = user.get("address")
        if address is not None:
            if not isinstance(address, dict):
                return False
            if not "city" in address or not isinstance(address.get("city"), str):
                return False
            if not "zip" in address or not isinstance(address.get("zip"), str):
                return False
        interests = user.get("interests")
        if interests is not None:
            if not isinstance(interests, list) or len(interests) < 1:
                return False
            for interest in interests:
                if not isinstance(interest, str):
                    return False
#------------------Сокращение------------------------------------------
        # if interests is not None:
        #     if not isinstance(interests, list) or not all(isinstance(i, str) for i in interests) or len(interests) == 0:
        #         return False
#-----------------------------------------------------------------------
        email = user.get("email")
        if email is not None:
            if not isinstance(email, str) or not "@" in email:
                return False
    return True
print(is_valid_user_list(users))