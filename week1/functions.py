# def great():
#     print('Hi, Denis')
# great()
#
# def great_user(name):
#     print("Hi,"+" " + name)
# great_user('Denis')
#
# def square(number):
#     return number * number
# print(square(5))
#
#
# #HW 1.1
#
# def say_hello():
#     print("Hello!")
# say_hello()
#
# #HW 1.2
# def add(a, b):
#     return a + b
# print(add(9, 10))
#
# #HW 1.3
# def is_even(number):
#     return number % 2 == 0
# print(is_even(4))
# print(is_even(7))
#
# #HW 2.1
#
# score = int(input("Enter your score from 0 to 100: "))
# def grade(score):
#     if score >= 90:
#         return "Awesome!"
#     elif score >= 80:
#         return "Perfect!"
#     elif score >= 60:
#         return "Good"
#     elif score >= 40:
#         return "Pass"
#     else:
#         return "Bad"
# print(grade(score))
#
# #HW 2.2

# def factorial(n):
#     result = 1
#     for i in range(1, n +1):
#         result *= i
#     return result
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))
# print(factorial(6))


#HW 2.3
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("hello"))
# print(reverse_string("Denis"))
# print(reverse_string("Python"))

#HW 3.1
# number = int(input("Enter a number: "))
# counter = number - 1
# def draw_square(n, c):
#     print(c)
#     for i in range(1, n + 1):
#         print(c * " " + (i + i - 1) * '*')
#         c -= 1
# draw_square(number, counter)

#HW 3.2
# user_number = int(input("Enter a number: "))
# def sum_even_numbers(num):
#     total = 0
#     for n in range(1, num + 1):
#         if n % 2 == 0:
#             total += n
#     return total
# print(sum_even_numbers(user_number))

#HW 3.3
# user_word = input("Enter a word: ")
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count
# print(count_vowels(user_word))

#HW 4.1
# def max_num(n):
#     max_number = n[0]
#     min_number = n[0]
#     for i in n:
#         if i > max_number:
#             max_number = i
#         if i < min_number:
#             min_number = i
#     avg_number = sum(n) / len(n)
#     return max_number, min_number, avg_number
# print(max_num([3, 5, 2, 8, 1]))
# print(max_num([-10, -5, -2, -8, -1]))


#HW 4.2
def analyze_list(lst):
    number_sum = 0
    even_number = 0
    avg_number = 0
    for i in lst:
        number_sum += i
        if i % 2 == 0:
            even_number +=1
    avg_number += number_sum / len(lst)
    return number_sum , even_number, avg_number
print(analyze_list([3, 5, 2, 8, 1, 4]))
print(analyze_list([-10, -5, -2, -8, -1]))