#Переменные в Python
name = "Denis"
age = 30
height = 1.89
is_learning = True

print(name, age, height, is_learning)
print(type(name), type(age), type(height), type(is_learning))

#Основные арифметические операции
a = 10
b =3

print("summ", a + b)
print("subtraction", a - b)
print("multiplication", a * b)
print("division", a / b)
print("integer division", a // b)
print("modulus", a % b)
print("exponentiation", a ** b)

#Конкатенация строк
greating = "Hello" + " " + name + "!"
print(greating)

#Преобразование типов
str_age = str(age)
float_age = float("3.14")
int_age = int("42")
print(str_age, float_age, int_age)

#
profile = {
    "name": name,
    "skils": ["Python", "JavaScript", "Git", "Linux"],
    "is_learning": is_learning,
    "goal": "Become a MLOps Engineer"
}
print(profile)
