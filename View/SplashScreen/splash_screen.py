from View.base_screen import BaseScreenView


class SplashScreenView(BaseScreenView):

    def change_screen(self, scr_name) -> None:
        self.manager_screens.current = scr_name

    def model_is_changed(self, option) -> None:
        pass
