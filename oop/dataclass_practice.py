#
# from dataclasses import dataclass, field, asdict
#
#
# @dataclass
# class User:
#     name: str
#     email: str
#     domain: str = field(init=False)
#     internal_id: int = field(default=42, compare=False)
#
#     def greet(self):
#         return f"Hello, my name is {self.name}"
#
#     def send_email(self, massage):
#         return f'Sending letter "{massage}" to {self.email}'
#
#     def set_new_name(self, new_name):
#         self.name = new_name
#
#     def __post_init__(self):
#         self.domain = self.email.split('@')[-1]
#
# user1 = User("Denis", "denis@email.com")
# user2 = User("Denis", "denis@email.com")
# print(user1)
# print(user1 == user2)
# print(user1.greet())
# user1.set_new_name("Денис")
# print(user1.name)
# print(user1.greet())
# print(user1.domain)
# user_dict = asdict(user1)
# print(user_dict)


# ----------------------------------------------------------------------------

from dataclasses import dataclass, field, asdict

@dataclass
class Adress:
    city: str
    street: str
    house_number: int

    def full_adress(self):
        return f"ул. {self.street}, дом {self.house_number}, город {self.city}"


@dataclass
class User:
    name: str
    email: str
    address: Adress
    domain: str = field(init=False)
    internal_id: int = field(default=0, compare=False)

    def __post_init__(self):
        self.domain = self.email.split('@')[-1]

u1 = User("Alice", "alice@gov.com", Adress("Springfield", "Main St", 123))
u2 = User("Alice", "alice@gov.com", Adress("Springfield", "Main St", 253))

print(u1 == u2)
print(asdict(u1))
print(asdict(u2))
print(u1.domain)
print(u1.address.full_adress())