import pytest

@pytest.fixture
def valid_user():
    return {"id": 1, "profile": {"name": "Bob", "email": "bob@example.com", "age": 25}}

@pytest.fixture
def invalid_user():
    return {"id": "abc","profile": {"name": "","email": "bobexample.com","age": 130}}