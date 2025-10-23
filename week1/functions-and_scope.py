#HW 1.1
# def greet_user(name):
#     return f"Hello, {name}!"
# print(greet_user("Denis"))

#HW 1.2
# def multiply(a, b):
#     return a * b
# print(multiply(4, 5))
#
# #HW 1.3
# def is_even(num):
#     return num % 2 == 0
# print(is_even(10))
# print(is_even(7))

#HW 2.1
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count
# print(count_vowels("Hello World"))
# print(count_vowels("Python Programming"))

#HW 2.2
# def apply_twice(func, value):
#     return func(func(value))
# def add_three(x):
#     return x ** 3
# print(apply_twice(add_three, 7))

#HW 2.3
# def safe_divide(a, b):
#     if b == 0:
#         return "Error: Division by zero"
#     return a / b
# print(safe_divide(10, 2))
# print(safe_divide(5, 0))

#HW 3.1
# towns = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Kiev"]
#
# def by_leng(lst):
#     return len(lst)
# print(sorted(towns, key=by_leng))

#HW 3.2
# def scope_test():
#     x = 10
#     print("Inside function, x =", x)
#     return x
# scope_test()
#
# y = 5
# print("Outside function, y =", y)

#HW 3.3
flags = str(input('choose and enter flag usa, ukraine, ru): '))
politic = input('Do you want a political greeting? (yes/no): ').strip().lower() == 'yes'
def build_greeting(flag, political):
    if political:
        if flag == 'usa':
            return "🇺🇸 Keep freedom and democracy strong!"
        elif flag == 'ukraine':
            return "🇺🇦 Stand with Ukraine for peace and sovereignty!"
        elif flag == 'ru':
            return "🇷🇺 We are a piece of shit!"
        else:
            return "Flag not recognized"
    else:
        if flag == 'usa':
            return "🇺🇸 Hello"
        elif flag == 'ukraine':
            return "🇺🇸 Slava Ukraini"
        elif flag == 'ru':
            return "🇷🇺 We are bitches"

print(build_greeting(flags, politic))
