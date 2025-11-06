
import pytest

import unittest_practice

@pytest.mark.parametrize("config, expected",[
    (
        {
            "meta": {"version": 1,"active": True},
            "modules": [{"name": "core", "enabled": True},{"name": "ui", "enabled": False}]
        },
        True
    ),
    (
        {
            "modules": [{"name": "core", "enabled": True}]
        },
        False
    ),
    (
        {
            "meta": {"version": "2", "active": True},
            "modules": [{"name": "core", "enabled": True}]
        },
        False
    ),
    (
        {
            "meta": {"version": "2", "active": True},
            "modules": [{"name": "core", "enabled": True}]
        },
        False
    ),
    (
        {
            "meta": {"version": 2, "active": True},
            "modules": []
        },
        False
    ),
    # (None, False),
    # ("not a dict", False),
    # ([], False),
])

def test_is_meta_valid_config(config, expected):
    assert unittest_practice.is_valid_meta_config(config) == expected


@pytest.mark.parametrize("config, expected",[
    (
        [
            {"id": 1, "name": "Alice", "profile": {"age": 30, "gender": "female"}},
            {"id": 2, "name": "Bob", "profile": {"age": 25, "gender": "male"}},
        ],
        True
    ),
    (
        [
            {"id": 1, "name": "Alice", "profile": {"age": 30, "gender": "female"}},
            {"id": 2, "name": "Bob", "profile": {"age": 25, "gender": "male"}},
            {"id": 3, "name": "Charlie", "profile": {"age": "unknown", "gender": None}}
        ],
        False
    ),
    (
        [
            {"name": "Alice", "profile": {"age": 30, "gender": "female"}},
        ],
        False
    ),
    (
        [
            {"id": 2, "name": "Bob", "profile": ["age", "male"]}
        ],
        False
    ),
    (
        [
            {"id": 1, "name": "Alice"}
        ],
        False
    ),
    (
        [
            {"id": 1, "name": "Alice", "profile": {"age": "30", "gender": None}}
        ],
        False
    ),
    # (None, False),
    # ("not a dict", False),
    # ([], False),

])

def test_is_valid_user_list(config, expected):
    assert unittest_practice.is_valid_user_list(config) == expected


@pytest.mark.parametrize("config, expected",[
    (
        [
            {"title": "Deploy", "done": False, "priority": 3},
            {"title": "Test", "done": True, "priority": 2},
        ],
        True
    ),
    (
        {
            "data":{"title": "Deploy", "done": False, "priority": 3}
        },
        False
    ),
    (
        [
            {"title": "Deploy", "done": 1, "priority": 3},
            {"title": "Test", "done": "True", "priority": 2},
        ],
        False
    ),
    # (None, False),
    # ("not a dict", False),
    # ([], False),
])

def test_is_valid_task_list(config, expected):
    assert unittest_practice.is_valid_task_list(config) == expected


@pytest.mark.parametrize("config, expected",[
    (
        {
            "name": "MyApp",
            "settings": {
                "theme": "dark",
                "autosave": True
            },
            "tags": ["stable", "v1"]
        },
        True
    ),
    (
        [{
            "name": "MyApp",
            "settings": {
                "theme": "dark",
                "autosave": True
            },
            "tags": ["stable", "v1"]
        }],
        False
    ),
    (
        {
            "settings": {
                "theme": "dark",
                "autosave": True
            },
            "tags": ["stable", "v1"]
        },
        False
    ),
    (
        {
            "name": "MyApp",
            "settings": {"theme": "dark", "autosave": True},
            "tags": "stable"
        },
        False
    ),
    # (None, False),
    # ("not a dict", False),
    # ([], False),
])

def test_is_valid_app_config(config, expected):
    assert unittest_practice.is_valid_app_config(config) == expected

valid_cart = {
    "config": {
        "meta": {"version": 1,"active": True},
        "modules": [{"name": "core", "enabled": True},{"name": "ui", "enabled": False}]
    },
    "users": [
        {"id": 1, "name": "Alice", "profile": {"age": 30, "gender": "female"}},
        {"id": 2, "name": "Bob", "profile": {"age": 25, "gender": "male"}},
    ],
    "tasks": [
        {"title": "Deploy", "done": False, "priority": 3},
        {"title": "Test", "done": True, "priority": 2},
    ],
    "app_config": {
        "name": "MyApp",
        "settings": {
            "theme": "dark",
            "autosave": True
        },
        "tags": ["stable", "v1"]
    }
}

@pytest.mark.parametrize("config, expected", [
    (valid_cart, True),
    ({}, False),
    (None, False),
    ("not a dict", False),
    (123, False),
    ([], False),
    ({**valid_cart, "config":{"meta":{"version": "1","active": True}}}, False),
    ({**valid_cart, "config":{"modules": [{"name": "core", "enabled": 1},{"name": "ui", "enabled": False}]}}, False),
    ({**valid_cart, "users": {"id": 3, "name": "Charlie", "profile": {"age": "unknown", "gender": None}}}, False),
    ({**valid_cart, "users": {"id": True, "name": "Charlie", "profile": {"age": "unknown", "gender": "male"}}}, False),
    ({**valid_cart, "tasks": [{"title": "", "done": "yes", "priority": -1}]}, False),
    ({**valid_cart, "tasks": {"title": "", "done": "yes", "priority": -1}}, False),
    ({**valid_cart, "app_config": {"settings": {"theme": "dark","autosave": True},"tags": ["stable", "v1"]}}, False),
    ({**valid_cart, "app_config": {"name": "MyApp","settings": {"theme": "dark","autosave": "yes"},"tags": ["stable", 1]}}, False)
])

def test_validate_cart(config, expected):
    assert unittest_practice.validate_cart(config) == expected