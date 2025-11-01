import unittest

from unittest_practice import *

class TestMetaConfigValidator(unittest.TestCase):
    def test_valid_config(self):
        """Корректная структура"""
        config = {
            "meta": {"version": 2, "active": True},
            "modules": [{"name": "core", "enabled": True}]
        }
        self.assertTrue(is_valid_meta_config(config))

    def test_missing_meta(self):
        """Нет ключа meta"""
        config = {
            "modules": [{"name": "core", "enabled": True}]
        }
        self.assertFalse(is_valid_meta_config(config))

    def test_wrong_version_type(self):
        """version — строка вместо int"""
        config = {
            "meta": {"version": "2", "active": True},
            "modules": [{"name": "core", "enabled": True}]
        }
        self.assertFalse(is_valid_meta_config(config))

    def test_empty_modules(self):
        """modules — пустой список"""
        config = {
            "meta": {"version": 2, "active": True},
            "modules": []
        }
        self.assertFalse(is_valid_meta_config(config))

    def test_module_missing_name(self):
        """Модуль без name"""
        config = {
            "meta": {"version": 2, "active": True},
            "modules": [{"enabled": True}]
        }
        self.assertFalse(is_valid_meta_config(config))

    def test_non_dict_input(self):
        """Вход — не словарь"""
        self.assertFalse(is_valid_meta_config(None))
        self.assertFalse(is_valid_meta_config(123))
        self.assertFalse(is_valid_meta_config("not a dict"))

class TestUserListValidator(unittest.TestCase):
    def test_valid_user_list(self):
        users_list = [
            {"id": 1, "name": "Alice", "profile": {"age": 30, "gender": "female"}},
            {"id": 2, "name": "Bob", "profile": {"age": 25, "gender": "male"}},
        ]
        self.assertTrue(is_valid_user_list(users_list))

    def test_non_id(self):
        usrrs_list = users_list = [
            {"name": "Alice", "profile": {"age": 30, "gender": "female"}},
        ]
        self.assertFalse(is_valid_user_list(usrrs_list))

    def test_wrong_type_profile(self):
        users_list = [
            {"id": 2, "name": "Bob", "profile": ["age", "male"]}
        ]
        self.assertFalse(is_valid_user_list(users_list))

    def test_non_list_input(self):
        self.assertFalse(is_valid_user_list(None))
        self.assertFalse(is_valid_user_list(123))
        self.assertFalse(is_valid_user_list("not list"))

    def test_missing_profile(self):
        users_list = [{"id": 1, "name": "Alice"}]
        self.assertFalse(is_valid_user_list(users_list))

    def test_profile_wrong_fields(self):
        users_list = [{"id": 1, "name": "Alice", "profile": {"age": "30", "gender": None}}]
        self.assertFalse(is_valid_user_list(users_list))


class TestTaskListValidator(unittest.TestCase):
    def test_valid_task_list(self):
        tasks = [
            {"title": "Deploy", "done": False, "priority": 3},
            {"title": "Test", "done": True, "priority": 2},
        ]
        self.assertTrue(is_valid_task_list(tasks))

    def test_non_list_input(self):
        tasks = {
            "data":{"title": "Deploy", "done": False, "priority": 3}
        }
        self.assertFalse(is_valid_task_list(tasks))

    def test_non_bool(self):
        tasks = [
            {"title": "Deploy", "done": 1, "priority": 3},
            {"title": "Test", "done": "True", "priority": 2},
        ]
        self.assertFalse(is_valid_task_list(tasks))

class TestAppConfigValidator(unittest.TestCase):
    def test_valid_app_config(self):
        config = {
            "name": "MyApp",
            "settings": {
                "theme": "dark",
                "autosave": True
            },
            "tags": ["stable", "v1"]
        }
        self.assertTrue(is_valid_app_config(config))

    def test_non_dict_input(self):
        config = [{
            "name": "MyApp",
            "settings": {
                "theme": "dark",
                "autosave": True
            },
            "tags": ["stable", "v1"]
        }]
        self.assertFalse(is_valid_app_config(config))

    def test_non_name(self):
        config = {
            "settings": {
                "theme": "dark",
                "autosave": True
            },
            "tags": ["stable", "v1"]
        }
        self.assertFalse(is_valid_app_config(config))

    def test_tags_wrong_type(self):
        config = {
            "name": "MyApp",
            "settings": {"theme": "dark", "autosave": True},
            "tags": "stable"
        }
        self.assertFalse(is_valid_app_config(config))


if __name__ == "__main__":
    unittest.main()