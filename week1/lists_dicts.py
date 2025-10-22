fruits = ["apple", "banana", "cherry", "date"]
# print(fruits[1])  # Output: banana
#
person = {"name": "Alice", "age": 30, "city": "New York"}
# print(person["age"])


#HW 1.1
# def get_last_element(lst):
#     if lst:
#         return lst[-1]
#     return "List is empty"
# print(get_last_element(fruits))

# #HW 1.2
# def sum_list(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     return sum
# print(sum_list([1, 2, 3, 4, 5]))
#--------------------------------------------
#сокращение через встроенную функцию sum

# def sum_list(lst):
#     return sum(lst)
# print(sum_list([1, 2, 3, 4, 5]))

#HW 1.3
# def filter_even_numbers(lst):
#     even_numbers = []
#     for i in lst:
#         if i % 2 == 0:
#             even_numbers.append(i)
#     return even_numbers
# print(filter_even_numbers([1, 2, 3, 4, 5, 6]))
# print(filter_even_numbers([7, 8, 9, 10, 11, 12]))

#HW 2.1
# def get_keys(d):
#     return list(d.keys())
# print(get_keys(person))

#HW 2.2
# def invert_dict(d):
#     inverted = {}
#     for key, value in d.items():
#         inverted[value] = key
#     return inverted
# print(invert_dict(person))

#HW 2.3
# def merge_dicts(d1, d2):
#     merged = d1.copy()
#     merged.update(d2)
#     return merged
# print(merge_dicts(person, {"occupation": "Engineer", "country": "USA"}))

#HW 3.1
# fruit_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
#
# def count_occurrences(lst):
#     new_dict = {}
#     for element in lst:
#         new_dict[element] = new_dict.get(element, 0) + 1
#     return new_dict
# print(count_occurrences(fruit_list))


#HW 3.2
# def  group_by_length(lst):
#     length_list = {}
#     for word in lst:
#         length = len(word)
#         length_list.setdefault(length, []).append(word)
#     return length_list
# print(group_by_length(fruits))


#HW 3.3
# squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# def find_max_value(d):
#     for key, value in d.items():
#         max_value = max(d.values())
#         if max_value == value:
#             return key
# print(find_max_value(squares))

#HW 4.1
text = "Python is powerful and Python is fun"

# def analyze_text(txt):
#     analyze_arr = {}
#     words = txt.split()
#     longest_word = ""
#     unique_word = {}
#     count = 0
#     for word in words:
#         unique_word[word] = unique_word.get(word, 0) + 1
#         if len(longest_word) < len(word):
#             longest_word = word
#         count = count + 1
#     analyze_arr["word count"] = count
#     analyze_arr["longest word"] = longest_word
#     analyze_arr["unique word"] = len(unique_word)
#     return analyze_arr
# print(analyze_text(text))

#HW 4.2
# d1 = {"a": 1, "b": 2, "c": 3}
# d2 = {"b": 2, "c": 4, "d": 5}
#
# def compaire_dicts(d1, d2):
#     new_arr = {}
#     set1 = set(d1)
#     set2 = set(d2)
#     common_keys = set1 & set2
#     new_arr["common_keys"] = list(common_keys)
#     new_arr["only_in_lst1"] = list(set1 - set2)
#     new_arr["only_in_lst1"] = list(set2 - set1)
#     new_arr["different_values"] = {
#         key: (d1[key], d2[key]) for key in common_keys if d1[key] != d2[key]
#     }
#     return new_arr
# print(compaire_dicts(d1, d2))

