#HW 1
#
# def  safe_divide(a, b):
#     try:
#          return print(a/b)
#     except ZeroDivisionError:
#         return print("ошибка - деление на ноль")
# safe_divide(1, 4)
# safe_divide(-8, -4)
# safe_divide(4, 0)

# HW 2
#
# path1 = "data/alice.json"
# path2 = "data/bob.json"
# path3 = "data/log.txt"
#
# def load_json(path):
#     try:
#         with open(path) as json_file:
#             return json.load(json_file)
#     except FileNotFoundError:
#         print("File not found")
#         return None
#     except json.decoder.JSONDecodeError:
#         print("Decoding error")
#         return None
#     finally:
#         print("File check finish")
# # load_json(path1)
# load_json(path2)
# # load_json(path3)

# HW 3
# users = [
#     {"name": "Alice", "role": "admin"},
#     {"name": "Bob", "role": "user"},
#     {"name": "Charlie"},
#     {"name": "Denis", "role": "admin"}
# ]
# def get_admins(data):
#         returm[user["name"]yt for user in data if user.get("role") == "admin"]
# print(get_admins(users))
#

user1 = {"email": "alice@example.com"}              # корректный email
user2 = {"email": None}                             # email есть, но None
user3 = {"email": 12345}                            # email есть, но не строка
user4 = {"name": "Bob"}                             # email отсутствует
user5 = {"email": "denis@dev.ua", "name": "Denis"}  # email + имя
user6 = {}

def extract_email(data):
    if isinstance(data.get("email"), str):
        return "Корректный email"
    else:
        return "Нет email"
print(extract_email(user1))
print(extract_email(user2))
print(extract_email(user3))
print(extract_email(user4))
print(extract_email(user5))
print(extract_email(user6))