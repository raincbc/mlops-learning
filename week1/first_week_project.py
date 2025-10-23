users = [
    {"name": "Alice", "age": 22, "city": "New York"},
    {"name": "Bob", "age": 35, "city": "Los Angeles"},
    {"name": "Charlie", "age": 27},
    {"name": "David", "age": 19, "city": "Chicago"},
    {"name": "Eve", "age": 45, "city": "Houston"},
    {"name": "Frank", "city": "Phoenix"},
    {"name": "Grace", "age": 18, "city": "Kiev"},
    {"name": "Hannah", "age": 40, "city": "Berlin"}
]

def analize_users(lst):
    total_users = len(lst)

    def get_over_30(data):
        return list(filter(lambda u: u.get('age', 0) > 30, data))

    def get_average_age(data):
        return round(sum(list(map(lambda u: u.get('age', 0), data))) / total_users, 2)

    def get_name_to_age(data):
        return {d["name"]: d["age"] for d in data if "name" in d and "age" in d}

    def get_long_names(data):
        return [u["name"] for u in data if len(u["name"]) > 5]

    def get_name_city_pairs(data):
        return [f'{u["name"]} -> {u.get("city", "Ukrnow")}' for u in data ]

    return {
        "total_users": total_users,
        "over_30": get_over_30(users),
        "average_age": get_average_age(users),
        "name_to_age": get_name_to_age(users),
        "long_names": get_long_names(users),
        "name_city_pairs": get_name_city_pairs(users),
    }
print(analize_users(users))