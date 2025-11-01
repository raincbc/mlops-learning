from tarfile import TruncatedHeaderError

import pytest

from unittest_practice import *

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
    (None, False),
    ("not a dict", False),
    ([], False),
])

def test_is_meta_valid_config(config, expected):
    assert is_valid_meta_config(config) == expected


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
    (None, False),
    ("not a dict", False),
    ([], False),

])

def test_is_valid_user_list(config, expected):
    assert is_valid_user_list(config) == expected


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
    (None, False),
    ("not a dict", False),
    ([], False),
])

def test_is_valid_task_list(config, expected):
    assert is_valid_task_list(config) == expected


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
    (None, False),
    ("not a dict", False),
    ([], False),
])

def test_is_valid_app_config(config, expected):
    assert is_valid_app_config(config) == expected
