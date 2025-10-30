#HW 1

config = {
    "model": {
        "name": "XGBoost",
        "description": "Gradient boosting model",
        "params": {
            "learning_rate": 0.1,
            "n_estimators": 100,
            "features": ["age", "income", "score"]
        }
    }
}

def is_valid_config(cfg):
    if not isinstance(cfg, dict):
        return False
    if not "model" in cfg:
        return False
    model = cfg.get("model")
    if  not isinstance(model, dict) or not isinstance(model['name'], str):
        return False
    description = model.get("description")
    if description is not None and not isinstance(description, str):
        return False
    if not "params" in model:
        return False
    params = model.get("params")
    if not isinstance(params, dict):
        return False
    if not "learning_rate" in params or not isinstance(params['learning_rate'], float):
        return False
    if not "n_estimators" in params or not isinstance(params['n_estimators'], int):
        return False
    if not "features" in params or not isinstance(params['features'], list) or len(params['features']) < 1:
        return False
    if not all(isinstance(item, str) for item in params['features']):
        return False
    return True
print(is_valid_config(config))

#HW 2

# broken_config = {
#     "model": {
#         "name": "XGBoost",
#         "params": {
#             "learning_rate": "0.1",  # ❌ строка вместо float
#             "n_estimators": 100,
#             "features": []
#         }
#     }
# }
# def is_broken_config(cfg):
#     if not isinstance(cfg.get("model", {}).get("params").get("learning_rate"), float):
#         return False
#     return True
# print(is_broken_config(broken_config))