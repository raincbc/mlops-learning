# HW 1
#
# user1 = {"profile": {"name": "Alice"}}
# user2 = {"profile": {"name": None}}
# user3 = {"profile": {}}
# user4 = {"account": {"name": "Bob"}}
# user5 = {}
# user6 = {"profile": {"name": "Denis", "age": 30}}
#
# def get_profile(user):
#     name = user.get("profile", {}).get("name")
#     return name if name else "Нет данных"
#
# print(get_profile(user1))
# print(get_profile(user2))
# print(get_profile(user3))
# print(get_profile(user4))
# print(get_profile(user5))
# print(get_profile(user6))
import profile
from queue import PriorityQueue

# HW 2
# em = "EM AIL @DeV . uA"
# def normalize_email(email):
#     if isinstance(email, str):
#         return email.lower().replace(" ", "")
# print(normalize_email(em))

# HW 3
#
# user1 = {"name": "Alice", "email": "alice@example.com", "active": True}
# user2 = {"name": "Bob", "email": "bob@example.com"}
# user3 = {"email": "charlie@example.com", "active": False}
# user4 = {"name": "Denis", "active": True}
# user5 = {"name": "Eva", "email": None, "active": True}
# user6 = {}
#
# def validate_user(data):
#     requred_keys = ["name", "email", "active"]
#     return all(key in data for key in requred_keys)
#     # C проверкой типов
#     # return (
#     #     isinstance(data.get("name"), str),
#     #     isinstance(data.get("email"), str),
#     #     isinstance(data.get("active"), bool),
#     # )
# print(validate_user(user1))
# print(validate_user(user2))
# print(validate_user(user3))
# print(validate_user(user4))
# print(validate_user(user5))
# print(validate_user(user6))


# Доп
# 1

# user = {"profile": {"name": "Denis", "age": 30}}
# def get_age(data):
#     if isinstance(data.get("profile", {}).get("age"), int):
#         return data["profile"]["age"]
# print(get_age(user))

#2
#
# order1 = {"id": 101, "items": ["apple", "banana"], "total": 25.5}         # ✅ валидный заказ
# order2 = {"id": 102, "items": [], "total": 0}                             # ❌ total не > 0
# order3 = {"id": "103", "items": "apple", "total": 10}                      # ❌ items не список
# order4 = {"id": 104, "items": ["milk"], "total": "10"}                   # ❌ total не число
# order5 = {"items": ["bread"], "total": 5.5}                              # ❌ нет id
# order6 = {"id": 105, "items": ["tea", "sugar"], "total": 15.0}           # ✅ валидный
# order7 = {"id": 106, "items": ["coffee"], "total": -3}                   # ❌ total отрицательный
# order8 = {"id": 107, "items": [], "total": 1}                            # ✅ валидный, пустой список допустим
#
# def validate_order(data):
#     validate_keys = ["id", "items", "total"]
#     # return all(key in data for key in validate_keys )
#     return (
#         isinstance(data.get("id"), int) and
#         isinstance(data.get("items"), list) and
#         isinstance(data.get("total"), (int, float)) and
#         data.get("total") > 0,
#     )
#
# print(validate_order(order1))
# print(validate_order(order2))
# print(validate_order(order3))
# print(validate_order(order4))
# print(validate_order(order5))
# print(validate_order(order6))
# print(validate_order(order7))
# print(validate_order(order8))

#  3

cart1 = [{"name": "apple", "price": 1.5}, {"name": "banana", "price": 2.0}]      # ✅
cart2 = [{"name": "milk", "price": 0}, {"name": "bread", "price": 1.2}]          # ❌ price = 0
cart3 = [{"name": "tea", "price": "2.5"}]                                        # ❌ price не число
cart4 = [{"name": "coffee"}]                                                    # ❌ нет price
cart5 = "not a list"                                                            # ❌ cart не список
cart6 = [{"name": "sugar", "price": 1.0}, {"name": None, "price": 2.0}]          # ❌ name не строка

# def validate_cart(cart):
#     if isinstance(cart, list):
#         for items in cart:
#                 if isinstance(items, dict):
#                     if isinstance(items.get("name"), str) and isinstance(items.get("price"), (int, float)) and items.get("price") > 0:
#                         continue
#                     else:
#                         return False
#                 else:
#                     return False
#         return True
#     else:
#         return False

# Сокращение
def validate_cart(cart):
    if not isinstance(cart, list):
        return False
    for items in cart:
        if not (
                isinstance(items, dict) and
                isinstance(items.get("name"), str) and
                isinstance(items.get("price"), (int, float)) and
                items.get("price") > 0
            ):
            return False
    return True

print(validate_cart(cart1))
print(validate_cart(cart2))
print(validate_cart(cart3))
print(validate_cart(cart4))
print(validate_cart(cart5))
print(validate_cart(cart6))