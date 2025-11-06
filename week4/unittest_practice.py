
config = {
    "meta": {
        "version": 1,
        "active": True
    },
    "modules": [
        {"name": "core", "enabled": True},
        {"name": "ui", "enabled": False}
    ]
}

def is_valid_meta_config(data):
    if not isinstance(data, dict):
        return False
    meta = data.get("meta")
    if not isinstance(meta, dict):
        return False
    version = meta.get("version")
    if not isinstance(version, int) or version < 1:
        return False
    if "active" not in meta or not isinstance(meta["active"], bool):
        return False
    modules = data.get("modules")
    if not isinstance(modules, list) or not all(isinstance(i, dict) for i in modules) or len(modules) == 0:
        return False
    for module in modules:
        if not "name" in module or len(module["name"]) == 0:
            return False
        if not "enabled" in module or not isinstance(module["enabled"], bool):
            return False
    return True
print(is_valid_meta_config(config))


# ------------------------------------------------------

users = [
    {"id": 1, "name": "Alice", "profile": {"age": 30, "gender": "female"}},
    {"id": 2, "name": "Bob", "profile": {"age": 25, "gender": "male"}},
    {"id": 3, "name": "Charlie", "profile": {"age": "unknown", "gender": None}}
]

def is_valid_user_list(user_list):
    if not isinstance(user_list, list):
        return False
    for user in user_list:
        if not "id" in user or not isinstance(user.get("id"), int):
            return False
        if not "name" in user or not isinstance(user.get("name"), str):
            return False
        profile = user.get("profile")
        if not isinstance(profile, dict):
            return False
        if not "age" in profile or not isinstance(profile["age"], int):
            return False
        if not "gender" in profile or not isinstance(profile["gender"], str):
            return False
    return True
print(is_valid_user_list(users))


# -------------------------------------------------

tasks = [
    {"title": "Deploy", "done": False, "priority": 3},
    {"title": "Test", "done": True, "priority": 2},
    {"title": "", "done": "yes", "priority": -1}
]
def is_valid_task_list(data):
    if not isinstance(data, list):
        return False
    for task in data:
        list_title = task.get("title")
        if not isinstance(list_title, str) or list_title == "":
            return False
        list_done = task.get("done")
        if not isinstance(list_done, bool):
            return False
        list_priority = task.get("priority")
        if not isinstance(list_priority, int) or list_priority < 0:
            return False
    return True
print(is_valid_task_list(tasks))

#------------------------------------------

config = {
    "name": "MyApp",
    "settings": {
        "theme": "dark",
        "autosave": True
    },
    "tags": ["stable", "v1"]
}
def is_valid_app_config(data):
    if not isinstance(data, dict):
        return False
    name = data.get("name")
    if not isinstance(name, str) or name == "":
        return False
    settings = data.get("settings")
    if not isinstance(settings, dict):
        return False
    if not "theme" in settings or not isinstance(settings.get("theme"), str):
        return False
    if not "autosave" in settings or not isinstance(settings.get("autosave"), bool):
        return False
    tags = data.get("tags")
    if tags is not None:
        if not isinstance(tags, list) or len(tags) == 0:
            return False
        if not all(isinstance(i, str) for i in tags):
            return False
    return True
print(is_valid_app_config(config))


def validate_cart(cart):
    if not isinstance(cart, dict):
        return False
    return (
        is_valid_meta_config(cart.get("config")) and
        is_valid_user_list(cart.get("users")) and
        is_valid_task_list(cart.get("tasks")) and
        is_valid_app_config(cart.get("app_config"))
    )