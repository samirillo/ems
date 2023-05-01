from Model.base_model import BaseScreenModel


class NewScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """
    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None

