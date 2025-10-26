
#HW 1

# import json
#
# with open("data/user.json") as f:
#     data = json.load(f)
#     print(data.get("name"))
#     print(data.get("profile", {}).get("city"))
#     print(data.get("email"))

#HW 2

# import json
#
# user = {
#     "name": "Alice",
#     "age": 25,
#     "skills": ["Python", "SQL"],
#     "profile": {"city": "Berlin", "active": False}
# }
#
# with open("data/alice.json", "w", encoding="utf-8") as outfile:
#     json.dump(user, outfile, indent=4, ensure_ascii=False)

#HW 3
#
# import json
#
# with open("data/users.json") as f:
#     data = json.load(f)
#     active_users = []
#     print(data)
#     for user in data:
#         is_active = user.get('profile', {}).get("active")
#         if is_active:
#             active_users.append(user["name"])
#     print(active_users)


#HW 4
#
# import json
#
# with open("data/logs.json") as json_file:
#     data = json.load(json_file)
#     count = {
#         "err_count": 0,
#         "info_count": 0,
#         "warning_count": 0
#     }
#     err_list = []
#     for elem in data:
#         if elem["type"] == "error":
#             err_list.append(elem)
#             count["err_count"] += 1
#         elif elem["type"] == "warning":
#             count["warning_count"] += 1
#         else:
#             count["info_count"] += 1
#     print(err_list, count)

#---------------------------------------------------
#Сокрfщенная альтернатива с библиотекой дефолтных словарей
import json
from collections import defaultdict

with open("data/logs.json") as json_file:
    data = json.load(json_file)
    count = defaultdict(int)
    err_list = []

    for elem in data:
        log_type = elem["type"]
        count[log_type] += 1
        if log_type == "error":
            err_list.append(elem)

    print(err_list)
    print(dict(count))  # Преобразуем обратно в обычный словарь для вывода