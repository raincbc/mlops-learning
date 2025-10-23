#HW 1.1
# squer = lambda x: x ** 2
# print(squer(5))
# print(squer(10))

#HW 1.2
# word = "madam"
# word2 = "hello"
# is_palindrome = lambda s: s == s[::-1]
# print(is_palindrome(word))
# print(is_palindrome(word2))

#HW 2.1
# nums  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# qubes = list(map(lambda x: x ** 3, nums))
# print(qubes)

#HW 2.2
# letters = ["Do", "you", "want", "a", "political", "greeting"]
# words_lengths = list(map(len, letters))
# print(words_lengths)

#HW 3.1
# random_nums = [10, -5, 3, -1, 0, 7, -8, 2]
# positive_nums = list(filter(lambda x: x > 0, random_nums))
# print(positive_nums)

#HW 3.2
# random_letters = ["apple", "banana", "cherry", "date", "fig", "grape"]
# long_words = list(filter(lambda s: len(s) > 5, random_letters))
# print(long_words)

#HW 4.1
# ages_list = [22, 35, 27, 19, 45, 30, 18, 40]
# names_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"]
# unification = list(zip(names_list, ages_list))
# print(unification)

#HW 4.2
key_list = ['name', 'age', 'city']
value_list = ['Alice', 30, 'New York']
dictionary = dict(zip(key_list, value_list))
print(dictionary)