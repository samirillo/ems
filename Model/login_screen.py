import multitasking

from Model.base_model import BaseScreenModel
from Utils.functions import validate_login_form,encriptar_password
multitasking.set_max_threads(10)


class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.LoginScreen.login_screen.LoginScreenView` class.
    """

    def __init__(self, database):
        self.database = database
        self.user_data = {}
        self._data_validation_status = None
        self._observers = []
        self.message=""
    @property
    def data_validation_status(self):
        return self._data_validation_status

    @data_validation_status.setter
    def data_validation_status(self, value):
        self._data_validation_status = value
        # We notify the View -
        # :class:`~View.LoginScreen.login_screen.LoginScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers()

    @multitasking.task
    def chek_data(self):
        """
        Get data from the database and compares this data with the data entered
        by the user.
        This method is completely asynchronous. It does not return any value.
        """
        response = validate_login_form(self.user_data)
        data_validation_status = False
        if response[0]:
            pwd_hash = encriptar_password(self.user_data["password"])
            self.user_data["password"] = pwd_hash  
            data= self.database.get_data_from_base_users(self.user_data)
            for key in data:
                print("#----dentro del for")
                print(data)
                print(self.user_data)
                if key == self.user_data:
                    data_validation_status = True
                    break
                else:
                    data_validation_status = False 
                    self.message="Usuario o contraseña invalidos" 
        else:
            self.message=response[1]
        
        self.data_validation_status = data_validation_status 

    def set_user_data(self, key, value):
        """Sets a dictionary of data that the user enters."""

        self.user_data[key] = value

    def notify_observers(self):
        """
        The method that will be called on the observer when the model changes.
        """

        for observer in self._observers:
            observer.model_is_changed(self.message)

    def reset_data_validation_status(self):
        self.data_validation_status = None

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)
