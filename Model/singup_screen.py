import multitasking

from Model.base_model import BaseScreenModel
from Utils.functions import validate_form, encriptar_password

multitasking.set_max_threads(10)


class SingupScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SingupScreen.singup_screen.SingupScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self.database = database
        self.user_data = {}

    def set_user_data(self, key, value):
        """Sets a dictionary of data that the user enters."""
        self.user_data[key] = value

    def create_user(self):
        response = validate_form(self.user_data)
        if response[0]:
            self.user_data.pop("confirm")
            pwd_hash = encriptar_password(self.user_data["password"])
            self.user_data["password"] = pwd_hash
            insert = self.database.insert(self.user_data)
            if insert:
                self.notify_observers("save")
            else:
                self.notify_observers("error al crear usuario ")
        else:
            self.notify_observers(response[1])

    def notify_observers(self, option):
        """
        The method that will be called on the observer when the model changes.
        """

        for observer in self._observers:
            observer.model_is_changed(option)

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
