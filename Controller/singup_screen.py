import importlib
from typing import NoReturn
import View.SingupScreen.singup_screen
from Utils.functions import encriptar_password

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.SingupScreen.singup_screen)


class SingupScreenController:
    """
    The `SingupScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.singup_screen.SingupScreenModel
        self.view = View.SingupScreen.singup_screen.SingupScreenView(controller=self, model=self.model)

    def set_user_data(self, key, value) -> NoReturn:
        self.model.set_user_data(key, value)

    def on_tap_button_signup(self):
        self.model.create_user()

    def on_tap_button_go_login(self, scr_name):
        self.view.change_screen(scr_name)

    def get_view(self) -> View.SingupScreen.singup_screen:
        return self.view
