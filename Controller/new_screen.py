from typing import NoReturn
import importlib

import View.NewScreen.new_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.NewScreen.new_screen)


class NewScreenController:

    def __init__(self, model):
        self.model = model
        self.view = View.NewScreen.new_screen.NewScreenView(controller=self, model=self.model)

    def on_tap_card(self) -> NoReturn:
        self.view.manager_screens.current = "main screen"

    def get_view(self) -> View.NewScreen.new_screen:
        return self.view
