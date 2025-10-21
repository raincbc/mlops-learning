# Демонстрация использования цикла for для перебора элементов списка и вывода их на экран.
# fruits = ["apple", "banana", "cherry", "date"]
# for fruit in fruits:
#     print("I like", fruit)

# Демонстрация использования цикла for с функцией range для выполнения определенного количества итераций.
# for i in range(5):
#     print("Iteration number:", i)

# Демонстрация использования цикла while для выполнения блока кода, пока условие истинно.
# counter = 0
# while counter < 5:
# #    print("Iteration number:", counter)
#     counter += 1

#HW 1.1
# for j in range(10 + 1):
#     print(j)

#HW 1.2
# for i in range(20 + 1):
#     if i > 0 and i % 2 == 0:
#         print(i)

#HW 1.3
# counter = 5
# while counter > 0:
#     print(counter)
#     counter -= 1

#HW 2.1
# num = int(input("Enter a number: "))
# sum = 0
#
# for i in range(1, num + 1):
#     sum += i
# print("The sum of numbers from 1 to", num, "is:", sum)

#HW 2.2
# word = "MLOps"
# for letter in word:
#     print(letter)

#HW 2.3
# num = int(input("Enter a number: "))
# while num > 0:
#     num = int(input("Enter a number: "))

#HW 3.1
# number = int(input("Enter a number: "))
# for i in range(1, number + 1):
#     print(i * '*')

#HW 3.2

number = int(input("Enter a number: "))
counter = number - 1
for i in range(1, number + 1):
    print(counter * " " + (i + i - 1) * '*')
    counter -= 1

