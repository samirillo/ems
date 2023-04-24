from typing import NoReturn
import importlib

import View.SettingScreen.setting_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.SettingScreen.setting_screen)


class SettingScreenController:

    def __init__(self, model):
        self.model = model
        self.view = View.SettingScreen.setting_screen.SettingScreenView(controller=self, model=self.model)

    def on_tap_card(self) -> NoReturn:
        self.view.manager_screens.current = "setting screen"

    def get_view(self) -> View.SettingScreen.setting_screen:
        return self.view