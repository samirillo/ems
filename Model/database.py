import os
from typing import Union
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError


class DataBase:
    """
    Your methods for working with the database should be implemented in this
    class.
    """

    def __init__(self):
        load_dotenv(find_dotenv())
        user = os.environ.get("MONGODB_ADDON_USER")
        password = os.environ.get("MONGODB_ADDON_PASSWORD")
        host = os.environ.get("MONGODB_ADDON_HOST")
        database = os.environ.get("MONGODB_ADDON_DATABASE")
        connection_string = "mongodb+srv://" + user + ":" + password + "@" + host + "/?retryWrites=true&w=majority"
        self.client = MongoClient(connection_string)

        self.db = self.client[database]

    def get_data_from_base_users(self, data: dict) -> Union[dict, None]:
        """
        Return data from the database:
        """
        try:
            cursor = self.db.users.find(data,{"_id":0,"email":1,"password":1})
        except PyMongoError as er:
            return None
        return cursor

    def insert(self, data: dict):
        try:
            self.db.users.insert_one(data)
            return True
        except PyMongoError as er:

            return False, er
