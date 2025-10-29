# 1

# user = {"name": "Alice", "email": "alice@example.com"}
#
# print(user.get("name", 0))
# print(user.get("email", "no-email"))

# 2

# config = {
#     "app": {
#         "settings": {
#             "language": "en"
#         }
#     }
# }
#
# print(config.get("app", {}).get("settings", {}).get("language", "ru"))

# 3

profiles = [
    {"name": "Alice", "details": {"age": 30}},
    {"name": "Bob"},
    {"name": "Charlie", "details": {"age": 25}}
]
result = []
for profile in profiles:
    result.append(profile.get("details", {}).get("age", 0))
print(result)
