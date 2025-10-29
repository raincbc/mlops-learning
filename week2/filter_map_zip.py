#HW 1
# users = [
#     {"name": "Alice", "active": True},
#     {"name": "Bob", "active": False},
#     {"name": "Charlie", "active": True}
# ]
# # filter_users = list(user["name"] for user in users if user["active"])
# # ------------------------------------сокращение
# print(list(map(lambda u: u["name"], filter(lambda u: u["active"], users))))
# --------------------------------------
# print(filter_users)

# HW 2

prices = [100, 200, 300]
discounts = [10, 20, 5]
#
# result = list(map(lambda n1, n2: n1 - ((n1 / 100) * n2), prices, discounts))
# ------------------------------сокращение
result = list(map(lambda p, d: p * (1 - d / 100), prices, discounts))
print(result)

# HW 3
#
# orders = [101, 102, 103]
# clients = ["Alice", "Bob", "Charlie"]
#
# result = dict(zip(orders, clients))
# print(result)