class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        return f"Hello, my name is {self.name}"

    def send_email(self, massage):
        return f'Sending letter "{massage}" to {self.email}'

    def set_new_name(self, new_name):
        self.name = new_name

user1 = User("Denis", "denis@example.com")
user2 = User("John", "john@example.com")

print(user1.name, user1.email)
print(user1.greet())
user1.set_new_name("Денис")
print(user1.name)
print(user1.send_email("Welcome to our platform!"))

print(user2.name, user2.email)
print(user2.greet())
print(user2.send_email("Your account has been created!"))