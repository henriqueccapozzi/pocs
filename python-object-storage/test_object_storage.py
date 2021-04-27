import os
import json

import pytest
from object_storage import DB


DB_FILE_NAME = "db.json"


def _create_test_db():
    return DB("test", file_name=DB_FILE_NAME)


def _create_mock_obj():
    return {
        "programing_languages_features": {
            "python": ["simple", "easy setup"],
            "javascript": ["widespread usage", "powerfull"],
        }
    }


class TestAtributes(object):
    def test_db_have_name(self):
        new_db = _create_test_db()
        assert new_db.name == "test"

    def test_insert_retrieve_objects(self):
        new_db = _create_test_db()
        new_db.insert(key="topic", value="registration")
        assert new_db.get("topic") == "registration"

        color_list = ["blue", "red", "green"]
        new_db.insert("color_list", color_list)
        assert new_db.get("color_list") == color_list

        new_db.insert("number", 9)
        assert new_db.get("number") == 9

        obj = _create_mock_obj()
        new_db.insert("languages", obj)
        assert new_db.get("languages") == obj

    def test_db_saves_to_file(self):
        new_db = _create_test_db()
        obj = _create_mock_obj()
        new_db.insert("languages", obj)
        new_db.save()
        assert os.stat("db.json") is not None

    def test_db_saves_proper_data_to_file(self):
        new_db = _create_test_db()
        obj = _create_mock_obj()
        new_db.insert("languages", obj)
        new_db.save()
        with open(DB_FILE_NAME, "r") as f:
            loaded_obj = json.load(f)
        assert loaded_obj == new_db.objects

    def test_db_loads_from_file(self):
        new_db = _create_test_db()
        new_db.insert("number", 1)
        new_db.save()

        loaded_db = DB("test", DB_FILE_NAME, True)
        assert loaded_db.objects == {"number": 1}