from tokenize import endpats

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     print(row)
#     for num in row:
#         print(num)

# person = {"name": "Alice", "age": 30, "city": ["New York",  "Los Angeles"]}
# for key, value in person.items():
#     print(f"{key}: {value}")
#


# HW 1.1
# def flatten_matrix(m):
#     flattened = []
#     for row in m:
#         for num in row:
#             flattened.append(num)
#     return flattened
# print(flatten_matrix(matrix))

# HW 1.2
# def sum_nested(m):
#     total = 0
#     for row in m:
#         for num in row:
#             total += num
#     return total
#
# print(sum_nested(matrix))

#-----------------------------------------
#сокращение через встроенную функцию sum
# def sum_nested(m):
#     return sum(sum(row) for row in m)
# print(sum_nested(matrix))

# HW 1.3
# def count_even_nested(m):
#     count = 0
#     for row in m:
#         for num in row:
#             if num % 2 == 0:
#                 count += 1
#     return count
# print(count_even_nested(matrix))

# HW 2.1
# arr = [{"a": 1, "b": 2}, {"c": 3, "d": 4}, {"e": 5, "f": 6}]
# def extract_values(s):
#     keys_list = []
#     for row in s:
#         for col in row:
#             keys_list.append(row[col])
#     return keys_list
# print(extract_values(arr))

# HW 2.2
# arr1 = {"a": 1, "b": 2, "h":{"c": 3, "d": 4}, "n":{"e": 5, "f": 6}}
# arr2 = {"x": 10, "y": 20, "h":{"g": 30, "z": 40}, "n":{"k":50 }}
# def merge_nested_dicts(d1, d2):
#     merged = d1.copy() | d2.copy()
#     for key in merged:
#         if key in arr1 and key in arr2:
#             if isinstance(d1[key], dict) and isinstance(d2[key], dict):
#                 merged[key] = {**d1[key], **d2[key]}
#     return merged
# print(merge_nested_dicts(arr1, arr2))

# HW 3.1
# def find_max_nested(m):
#     max_value = max(max(row) for row in m)
#     return max_value
# print(find_max_nested(matrix))

# HW 3.2
# data_list = [1, "a", 2.5, "b"]
# def separate_types(lst):
#     int_list = []
#     str_list = []
#     float_list = []
#     for item in lst:
#         if isinstance(item, int):
#             int_list.append(item)
#         elif isinstance(item, str):
#             str_list.append(item)
#         elif isinstance(item, float):
#             float_list.append(item)
#     return {"int": int_list, "str": str_list, "float": float_list}
# print(separate_types(data_list))

# HW 3.3
my_dict = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f":{"g": 5, "k":{"i":17}}}}, "h": 4}
# def deep_count(d):
#     count = 0
#     for key, value in d.items():
#         count += 1
#         if isinstance(value, dict):
#             count += deep_count(value)
#     return count
# print(deep_count(my_dict))

#HW 4.1
def analyze_nested_dict(d, prefix=""):
    analyze_arr = {
        "total_keys": 0,
        "max depth": 0,
        "unique_values": set(),
        "path to values": []
    }
    for key, value in d.items():
        analyze_arr["total_keys"] += 1
        full_key = f"{prefix}.{key}" if prefix else key

        if isinstance(value, dict):
            nested_analysis = analyze_nested_dict(value, full_key)
            analyze_arr["path to values"] += nested_analysis["path to values"]
            analyze_arr["total_keys"] += nested_analysis["total_keys"]
            analyze_arr["max depth"] = max(analyze_arr["max depth"], 1 + nested_analysis["max depth"])
            analyze_arr["unique_values"].update(nested_analysis["unique_values"])
        else:
            analyze_arr["path to values"].append(f"{full_key} → {value}")
            analyze_arr["unique_values"].add(value)
    return analyze_arr
print(analyze_nested_dict(my_dict))


#HW 4.2
# def get_paths(d, prefix=""):
    # paths = []
    # for key, value in d.items():
    #     full_key = f"{prefix}.{key}" if prefix else key
#         if isinstance(value, dict):
#             paths.extend(get_paths(value, full_key))
#         else:
#             paths.append(f"{full_key} → {value}")
#     return paths
# print(get_paths(my_dict))
