#Условные операторы if-else в Python
temperature = 18
if temperature > 20:
    print("It's a warm day")
else:
    print("It's a cold day")

# Пример с использованием elif
score = 85
if score >= 90:
    print("Awesome!")
elif score >= 75:
    print("Well done!")
elif score >= 50:
    print("You passed")
else:
    print("Better luck next time")


# Вложенные условия
age = 25
has_id = True
if age >= 18:
    if has_id:
        print("You can enter the club")
    else:
        print("You need an ID to enter the club")
else:
    print("You are too young to enter the club")

# Логические операторы
is_administrator = True
is_logged_in = False

if is_administrator and is_logged_in:
    print("Welcome, Admin!")
else:
    print("Axess Denied")

# Проверка на четность
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")