
import os
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
        connection_string = "mongodb+srv://"+user+":"+password+"@"+host+"/?retryWrites=true&w=majority"
        self.client = MongoClient(connection_string)

        self.db =self.client[database]

    def insert(self, data: dict) -> bool:
        try:
            self.db.users.insert_one(data)
            return True
        except PyMongoError as er:
            print(er)
            return False

