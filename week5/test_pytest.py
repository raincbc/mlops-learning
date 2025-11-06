import pytest
from fixture_practice import is_valid_user_profile

def test_valid_user_profile(valid_user):
    assert is_valid_user_profile(valid_user)

def test_invalid_user_profile(invalid_user):
    assert not is_valid_user_profile(invalid_user)

def test_non_dict_input():
    assert not is_valid_user_profile("not a dict")
    assert not is_valid_user_profile(123)
    assert not is_valid_user_profile(["list"])

def test_profile_not_dict():
    data = {"id": 1, "profile": "not a dict"}
    assert not is_valid_user_profile(data)

def test_name_invalid():
    data = {"id": 1, "profile": {"name": "", "email": "bob@example.com", "age": 25}}
    assert not is_valid_user_profile(data)

    data["profile"]["name"] = None
    assert not is_valid_user_profile(data)

    data["profile"]["name"] = 123
    assert not is_valid_user_profile(data)

def test_email_invalid():
    data = {"id": 1, "profile": {"name": "Bob", "email": "bobexample.com", "age": 25}}
    assert not is_valid_user_profile(data)

    data["profile"]["email"] = None
    assert not is_valid_user_profile(data)

def test_age_invalid():
    data = {"id": 1, "profile": {"name": "Bob", "email": "bob@example.com", "age": 130}}
    assert not is_valid_user_profile(data)

    data["profile"]["age"] = -5
    assert not is_valid_user_profile(data)

    data["profile"]["age"] = "25"
    assert not is_valid_user_profile(data)
