from typing import NoReturn

import View.LoginScreen.login_screen


class LoginScreenController:
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.view = View.LoginScreen.login_screen.LoginScreenView(controller=self, model=self.model)

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

        self.model.set_user_data(key, value)

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""
        self.view.show_dialog_wait()
        self.model.chek_data()

    def reset_data_validation_status(self, *args) -> NoReturn:
        self.model.reset_data_validation_status()

    def on_tap_button_go_signup(self, scr_name):
        self.view.change_screen(scr_name)

    def get_view(self) -> View.LoginScreen.login_screen:
        return self.view
