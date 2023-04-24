from typing import NoReturn
import importlib

import View.UpdateScreen.update_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.UpdateScreen.update_screen)


class UpdateScreenController:

    def __init__(self, model):
        self.model = model
        self.view = View.UpdateScreen.update_screen.UpdateScreenView(controller=self, model=self.model)

    def on_tap_card(self) -> NoReturn:
        self.view.manager_screens.current = "update screen"

    def get_view(self) -> View.UpdateScreen.update_screen:
        return self.view