import datetime
from kivy.properties import ObjectProperty
from View.base_screen import BaseScreenView


class SingupScreenView(BaseScreenView):
    controller = ObjectProperty()
    """
    Controller object - :class:`~Controller.login_screen.LoginScreenController`.
    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.login_screen.LoginScreenModel`.
    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    manager_screens = ObjectProperty()
    """
    Screen manager object - :class:`~kivy.uix.screenmanager.ScreenManager`.
    :attr:`manager_screens` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """
    date = datetime.datetime.now()
    def __init__(self, **kw):
        super().__init__(**kw)

    def change_screen(self, scr_name) -> None:
        self.manager_screens.current = scr_name

    def model_is_changed(self, option) -> None:
       if option == "equal":
           print("contraseñas iguales")
       elif option =="save":
           print("usuario creado con exito")
       else:
            self.ids.message.text=option
