# # HW 1
# from pygments.lexers import data
#
# config = {
#     "meta": {
#         "version": 1,
#         "active": True
#     },
#     "modules": [
#         {"name": "core", "enabled": True},
#         {"name": "ui", "enabled": False}
#     ]
# }
#
# def is_valid_meta_config(data):
#     meta = data.get("meta")
#     if not isinstance(meta, dict):
#         return False
#     if "version" not in meta or meta["version"] < 1:
#         return False
#     if "active" not in meta or not isinstance(meta["active"], bool):
#         return False
#     modules = data.get("modules")
#     if not isinstance(modules, list) or not all(isinstance(i, dict) for i in modules) or len(modules) == 0:
#         return False
#     for module in modules:
#         if not "name" in module or len(module["name"]) == 0:
#             return False
#         if not "enabled" in module or not isinstance(module["enabled"], bool):
#             return False
#     return True
# print(is_valid_meta_config(config))
#
# # assert is_valid_meta_config([{"meta": {"version": 1, "active": True}}])  == False
# # assert is_valid_meta_config({"meta": {"version": 10, "active": True},"modules": [{"name": "core", "enabled": False}]}) == True
# # assert is_valid_meta_config({"meta": {"version": 1.2, "active": 2},"modules": [{"name": "core", "enabled": "False"}]}) == False
#
# # HW 2
# users = [
#     {"id": 1, "name": "Alice", "profile": {"age": 30, "gender": "female"}},
#     {"id": 2, "name": "Bob", "profile": {"age": 25, "gender": "male"}},
#     {"id": 3, "name": "Charlie", "profile": {"age": "unknown", "gender": None}}
# ]
#
# def is_valid_user_list(user_list):
#     for user in user_list:
#         if not "id" in user or not isinstance(user.get("id"), int):
#             return False
#         if not "name" in user or not isinstance(user.get("name"), str):
#             return False
#         profile = user.get("profile")
#         if not isinstance(profile, dict):
#             return False
#         if not "age" in profile or not isinstance(profile["age"], int):
#             return False
#         if not "gender" in profile or not isinstance(profile["gender"], str):
#             return False
#     return True
# print(is_valid_user_list(users))
#
# assert is_valid_user_list([{"id": 123, "name": "Alice", "profile": {"age": 45, "gender": "female"}}]) == True
# assert is_valid_user_list([]) == False
# assert is_valid_user_list({"id": 2, "name": "Bob", "profile": {"age": 25, "gender": "male"}})
#
# # HW 3
# tasks = [
#     {"title": "Deploy", "done": False, "priority": 3},
#     {"title": "Test", "done": True, "priority": 2},
#     {"title": "", "done": "yes", "priority": -1}
# ]
# def is_valid_task_list(data):
#     for task in data:
#         list_title = task.get("title")
#         if not isinstance(list_title, str) or list_title == "":
#             return False
#         list_done = task.get("done")
#         if not isinstance(list_done, bool):
#             return False
#         list_priority = task.get("priority")
#         if not isinstance(list_priority, int) or list_priority < 0:
#             return False
#     return True
# print(is_valid_task_list(tasks))
#
# # assert is_valid_task_list([[1, True, "list"], [], ["name"]]) == False
# # assert is_valid_task_list([{"title": "Replay", "done": True, "priority": 17}]) == True
# # assert is_valid_task_list({"title": "", "done": "yes", "priority": -1}) == False
#
# # #HW 4
# config = {
#     "name": "MyApp",
#     "settings": {
#         "theme": "dark",
#         "autosave": True
#     },
#     "tags": ["stable", "v1"]
# }
# def is_valid_app_config(data):
#     name = data.get("name")
#     if not isinstance(name, str) or name == "":
#         return False
#     settings = data.get("settings")
#     if not isinstance(settings, dict):
#         return False
#     if not "theme" in settings or not isinstance(settings.get("theme"), str):
#         return False
#     if not "autosave" in settings or not isinstance(settings.get("autosave"), bool):
#         return False
#     tags = data.get("tags")
#     if tags is not None:
#         if not isinstance(tags, list) or len(tags) == 0:
#             return False
#         if not all(isinstance(i, str) for i in tags):
#             return False
#     return True
# print(is_valid_app_config(config))
#
# # assert is_valid_app_config({"123":None}) == False
# # assert is_valid_app_config({"name": "MyApp","settings": {"theme": "blue","autosave": False},"tags": ["stable", "v5"]}) == True
# # assert is_valid_app_config({}) == False
