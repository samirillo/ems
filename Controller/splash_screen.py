import importlib

import View.SplashScreen.splash_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.SplashScreen.splash_screen)


class SplashScreenController:
    """
    The `SplashScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.splash_screen.SplashScreenModel
        self.view = View.SplashScreen.splash_screen.SplashScreenView(controller=self, model=self.model)

    def on_tap_button_login(self, scr_name):
        self.view.change_screen(scr_name)



    def get_view(self) -> View.SplashScreen.splash_screen:
        return self.view
