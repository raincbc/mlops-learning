from dataclasses import field

from pydantic import BaseModel, Field, ValidationError, field_validator


# class Address(BaseModel):
#     street: str
#     city: str
#     zip_code: str
#
# class User(BaseModel):
#     name: str
#     email: str
#     age: int
#     address: Address
#
# u1 = User(name="Alice", email="alice@ukr.net", age=30, address={"street": "Baker St", "city": "London", "zip_code": "NW1 6XE"})
# print(u1)
# print(u1.address)
# print(u1.model_dump(mode="dict"))
# print(u1.model_validate({"name": "Bob", "email": "bob@u.net", "age": 25, "address": {"street": "5th Ave", "city": "New York", "zip_code": "10001"}}))
# new_user = u1.model_copy(update={"age": 33})
# print(u1.age, new_user.age)
# try:
#     u2 = User(name="Bob", email=123, age="35")
#     u3 = User(name="Charlie", email="charlie@gret,com", age="thirty", address={"street": "Elm St", "city": "Springfield", "zip_code": "62704"})
# except ValidationError as e:
#     print("Validation error:", e)


class Adress(BaseModel):
    zip_code: str

    @field_validator("zip_code")
    def validate_zip_code(cls, value):
        if not value.isdigit() or len(value) < 5:
            raise ValueError("Zip code must be a 5-digit number")
        return value


class User(BaseModel):
    age: int
    email:str
    adress:Adress

    @field_validator("email", mode="before")
    def validate_email(cls, value):
        if value.split('@')[-1] == "example.com":
            raise ValueError("Invalid email address")
        return value

    @field_validator("age")
    def validate_age(cls, value):
        if value < 18 or value > 120:
            raise ValueError("Age must be at least 18")
        return value
try:
    u1 = User(email="denis@example.com", age=25, adress={"zip_code": "1234"})
    print(u1)
except ValidationError as e:
    print("Validation error:", e)

try:
    u2 = User(email="denis@ukr.net", age=30, adress={"zip_code": "12345"})
    print(u2)
except ValidationError as e:
    print("Validation error:", e)

try:
    u3 = User(email="sfdghlj@dhs.fgh", age=15, adress={"zip_code": "67890h"})
    print(u3)
except ValidationError as e:
    print("Validation error:", e)

try:
    u4 = User(email="sfdghljtyutyut@dhs.fgh", age=40, adress={"zip_code": "67896"})
    print(u4)
except ValidationError as e:
    print("Validation error:", e)




