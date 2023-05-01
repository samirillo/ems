import datetime
import os
import socket
import time

from dotenv import load_dotenv
from supabase import Client, create_client


def get_time() -> str:
    """Returns a string with the current date and time."""

    return datetime.datetime.fromtimestamp(
        time.mktime(datetime.datetime.now().timetuple())
    ).strftime("%d-%m-%Y %H:%M:%S")


def get_connect(func, host="8.8.8.8", port=53, timeout=3):
    """Checks for an active Internet connection."""

    def wrapped(*args):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                (host, port)
            )
            return func(*args)
        except Exception as e:
            print(e)
            return False

    return wrapped


class DataBase:
    """
    Your methods for working with the database should be implemented in this
    class.
    """

    def __init__(self):
        load_dotenv(".env")
        self.url: str = os.environ.get("SUPABASE_URL")
        self.key: str = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(self.url, self.key)

    def insert_user(self, data: dict) -> bool:
        image = []
        updated = get_time()
        avt = data["avatar"]
        image = avt.split(sep='/')
        try:
            user = self.supabase.auth.sign_up(email=data["email"], password=data["password"])
            avatar = self.upload_avatar(str(user.id)+"/"+str(image[len(image)-1]), data["avatar"])
            self.create_user_profile(user.id, updated, data["full_name"], avatar, "True")
            print(user.user_metadata.get("full_name"))
            return True
        except Exception as er:
            print("create user: " + str(er))
            return False

    def create_user_profile(self, user_id, updated, fullname, avatar, res):
        data = {"id": user_id, "updated_at": updated, "full_name": fullname, "avatar_url": avatar, "is_admin": res}
        print(data[0])
        try:
            profile = self.supabase.table("perfiles").insert([{"id": user_id["UUID"], "updated_at": updated, "full_name": fullname, "avatar_url": avatar, "is_admin": res}]).execute()
        except Exception as e:
            print("create profile " + str(e))

    def upload_avatar(self, path, file):
        try:
            avatar = self.supabase.storage().from_("avatars").upload(path, file)
            return avatar.url.path
        except Exception as e:
            print("upload avatar: "+str(e))