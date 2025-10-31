config = {
    "version": 2,
    "debug": True,
    "services": [
        {"name": "auth", "enabled": True, "retries": 3},
        {"name": "db", "enabled": False, "retries": 0}
    ],
    "tags": ["prod", "critical"]
}

def is_valid_config(cfg):
    version = cfg.get("version")
    if not isinstance(version, int) or version < 1:
        return False
    debug = cfg.get("debug")
    if not isinstance(debug, bool):
        return False
    services = cfg.get("services")
    if not isinstance(services, list) or not all(isinstance(i, dict) for i in services):
        return False
    for service in services:
        print(service)
        if not "name" in service or not isinstance(service["name"], str) or len(service["name"]) == 0:
            return False
        if not "enabled" in service or not isinstance(service["enabled"], bool):
            return False
        if not "retries" in service or not isinstance(service["retries"], int) or service["retries"] < 0:
            return False
    tags = cfg.get("tags")
    if tags is not None:
        if not isinstance(tags, list) or not all(isinstance(i, str) for i in tags) or len(tags) == 0:
            return False
    return True
print(is_valid_config(config))