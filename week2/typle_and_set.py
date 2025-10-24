# coordinates = [(1, 2), (3, 4), (5, 6)]
# for x, y in coordinates:
#     print(x + y)
#
from itertools import count
from shlex import split
from tkinter.font import names

# numbers = {2, 4, 6, 6, 2, 8}
# print(len(numbers))

#HW 1.1
tuple_list = [("Alice", 25), ("Denis", 39), ("Mary", 33), ("Ann", 19)]
# age = 0
# user_count = 0
# for element in tuple_list:
#     if element[1]:
#         age += element[1]
#         user_count += 1
#     print(element[0])
# print(age / user_count)

#----------------------------------
#сокращение

# names = [ name for name, _ in tuple_list]
# print(names)
#
# average_age = sum(age for _, age in tuple_list) / len(tuple_list)
# print(round(average_age, 2))


# # Средний возраст
# average_age = sum(age for _, age in tuple_list) / len(tuple_list)
# print(round(average_age, 2))

#HW 2.1
# a = ["apple", "banana", "cherry", "apple"]
# b = ["banana", "date", "fig", "banana"]
#
# print(set(set(a) - set(b) | set(b) - set(a)))
# print(set(a) & set(b))
# print(set(a) - set(b))


#HW 3.1
# users = [
#     {"name": "Alice", "contacts": {"email": "alice@example.com"}},
#     {"name": "Bob"},
#     {"name": "Charlie", "contacts": {"email": "charlie@example.com"}}
# ]
# users_name = []
# users_email = []
# users_with_em_count = 0
# for user in users:
#     users_name.append(user["name"])
#
#     if "contacts"in user:
#     # if user.get("contacts") and "email" in user["contacts"]:   #альтернатива
#         users_email.append(user["contacts"]["email"])
#         users_with_em_count += 1
#
#
# print(users_name, users_email, users_with_em_count)

users = [
    ("Alice", 25, "New York"),
    ("Bob", 30, "Los Angeles"),
    ("Charlie", 22, "Chicago"),
    ("Denis", 39, "Kiev"),
    ("Eve", 45, "Berlin")
]

old_users = [f'{name}' for name, age, _ in users if age > 30]
users_town = [f'{name} live in {city}' for name, _, city in users ]
average_age = sum(age for _, age, _ in users) / len(users)
print(round(average_age, 2))
print(users_town)
print(old_users)