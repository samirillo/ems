from typing import NoReturn, Union

from kivy.clock import Clock
from kivy.properties import ObjectProperty

from kivymd.theming import ThemableBehavior
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from View.base_screen import BaseScreenView


class LoginScreenView(BaseScreenView):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.dialog = MDDialog()
        self.dialog.bind(on_dismiss=self.controller.reset_data_validation_status)
        self.model.add_observer(self)

    def show_dialog_wait(self) -> NoReturn:
        """Displays a wait dialog while the model is processing data."""

        self.dialog.auto_dismiss = False
        self.dialog.text = "Data validation..."
        self.dialog.open()

    def show_toast(self, interval: Union[int, float]) -> NoReturn:
        Snackbar(
            text="¡Usuario verificado con éxito!",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.8,
            bg_color=self.theme_cls.primary_color,
        ).open()

    def model_is_changed(self,message) -> NoReturn:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

        if self.model.data_validation_status:
            self.dialog.dismiss()
            Clock.schedule_once(self.show_toast, 1)
            Clock.schedule_once(self.go_main_screen, 5)
        if self.model.data_validation_status is False:
            self.dialog.text = message
            self.dialog.auto_dismiss = True


    def go_main_screen(self, *args):
        self.manager_screens.current = "main screen"