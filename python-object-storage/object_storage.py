import json


class DB(object):
    def __init__(self, name, file_name, load_from_file=False):
        self.__name = name
        self.__file_name = file_name
        self.__db = {}

        if load_from_file:
            with open(file_name, "r") as f:
                self.__db = json.load(f)

    @property
    def name(self):
        return self.__name

    @property
    def objects(self) -> dict:
        return self.__db

    def insert(self, key, value):
        self.__db[key] = value

    def save(self):
        with open(self.__file_name, "w") as f:
            json.dump(self.__db, f)
            return True

    def get(self, key):
        return self.__db.get(key, None)