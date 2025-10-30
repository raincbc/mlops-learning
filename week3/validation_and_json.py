#HW 1
# config = {
#     "model": {
#         "name": "XGBoost",
#         "params": {
#             "learning_rate": 0.1,
#             "n_estimators": 100
#         }
#     }
# }
#
# def is_valid_config(cfg):
#     if not isinstance(cfg, dict):
#         return False
#     if not "model" in cfg or not cfg.get("model", {}).get("params"):
#         return False
#     params = cfg.get("model", {}).get("params")
#     if not params.get("learning_rate") or not params.get("n_estimators"):
#         return False
#     return True
# print(is_valid_config(config))

#HW 2
broken_config = {
    "model": {
        "params": {
            "n_estimators": 100
        }
    }
}

def is_valid_config(cfg):
    params = cfg.get("model", {}).get("params")
    if not isinstance(params, dict):
        return False
    if not params.get("learning_rate"):
        return False
    return True
print(is_valid_config(broken_config))