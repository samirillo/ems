from typing import NoReturn
import importlib


import View.MainScreen.main_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.MainScreen.main_screen)


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = View.MainScreen.main_screen.MainScreenView(controller=self, model=self.model)

    def on_slide_progress(self, instance_carousel, offset_value):
        """
        Called when the user swipes on the screen (the moment the slides move).
        """

        self.view.do_animation_card_content(instance_carousel, offset_value)

    def get_view(self) -> View.MainScreen.main_screen.MainScreenView:
        return self.view
