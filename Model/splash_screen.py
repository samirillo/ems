import multitasking

from Model.base_model import BaseScreenModel

multitasking.set_max_threads(10)


class SplashScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SplashScreen.splash_screen.SplashScreenView` class.
    """

    def __init__(self, database):
        self.database = database

