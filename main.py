
from heapq import merge
from kivymd.tools.hotreload.app import MDApp
from kivy.core.window import Window
import importlib
import os
from typing import NoReturn

from kivy import Config
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer

from PIL import ImageGrab
from kivy.core.text import LabelBase
from kivy.properties import DictProperty

from kivymd.font_definitions import theme_font_styles
# TODO: You may know an easier way to get the size of a computer display.
resolution = ImageGrab.grab().size

# Change the values of the application window size as you need.
Config.set("graphics", "height", resolution[1])
Config.set("graphics", "width", "200")


# Place the application window on the right side of the computer screen.
#Window.top = 0
# Window.left = resolution[0] - 1840
Window.left = resolution[0] - 1400
Window.size = 800, 667


class emsApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = ScreenManager()

    def build_app(self) -> ScreenManager:
        """
        In this method, you don't need to change anything other than the
        application theme.
        """
        import View.screens
        """
        Custom colors
        """
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "300"
        self.theme_cls.primary_dark_hue = "700"
        self.theme_cls.accent_palette = "Green"
        self.theme_cls.accent_hue = "100"
        """
        Add fonts to themes 
        """
        LabelBase.register(
            name="Poppins",
            fn_regular="./assets/fonts/Poppins-Regular.ttf")
        LabelBase.register(
            name="Poppins-Bold",
            fn_regular="./assets/fonts/Poppins-Bold.ttf")
        font_styles = {
            "Body1": ["Poppins", 16, False, 0.15],
            "Bold": ["Poppins-Bold", 16, False, 0.15],
            "H5": ["Poppins", 24, False, 0],
            "H3": ["Poppins", 48, False, 0],
        }
        self.theme_cls.font_styles.update(font_styles)
        """
        Add NavigationLayout - Drawer - ScreenManager
        """
        self.manager_screens = ScreenManager()
        self.navigation_layout = MDNavigationLayout()
        self.navigation_drawer = MDNavigationDrawer()

        Window.bind(on_key_down=self.on_keyboard_down)
        importlib.reload(View.screens)
        screens = View.screens.screens

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)

        self.navigation_layout.add_widget(self.manager_screens)
        self.navigation_layout.add_widget(self.navigation_drawer)
        #self.manager_screens.current = "plagas screen"
        return self.navigation_layout

    def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> NoReturn:
        """
        The method handles keyboard events.

        By default, a forced restart of an application is tied to the
        `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
        """

        if "meta" in modifiers or "ctrl" in modifiers and text == "r":
            self.rebuild()


emsApp().run()

# After you finish the project, remove the above code and uncomment the below
# code to test the application normally without hot reloading.

# """
# The entry point to the application.
#
# The application uses the MVC template. Adhering to the principles of clean
# architecture means ensuring that your application is easy to test, maintain,
# and modernize.
#
# You can read more about this template at the links below:
#
# https://github.com/HeaTTheatR/LoginAppMVC
# https://en.wikipedia.org/wiki/Model–view–controller
# """
#
# from typing import NoReturn
#
# from kivy.uix.screenmanager import ScreenManager
#
# from kivymd.app import MDApp
#
# from View.screens import screens
#
#
# class vergel(MDApp):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.load_all_kv_files(self.directory)
#         # This is the screen manager that will contain all the screens of your
#         # application.
#         self.manager_screens = ScreenManager()
#
#     def build(self) -> ScreenManager:
#         """
#         Initializes the application; it will be called only once.
#         If this method returns a widget (tree), it will be used as the root
#         widget and added to the window.
#
#         :return:
#             None or a root :class:`~kivy.uix.widget.Widget` instance
#             if no self.root exists.
#         """
#
#         self.theme_cls.primary_palette = "Amber"
#         self.generate_application_screens()
#         return self.manager_screens
#
#     def generate_application_screens(self) -> NoReturn:
#         """
#         Creating and adding screens to the screen manager.
#         You should not change this cycle unnecessarily. He is self-sufficient.
#
#         If you need to add any screen, open the `View.screens.py` module and
#         see how new screens are added according to the given application
#         architecture.
#         """
#
#         for i, name_screen in enumerate(screens.keys()):
#             model = screens[name_screen]["model"]()
#             controller = screens[name_screen]["controller"](model)
#             view = controller.get_view()
#             view.manager_screens = self.manager_screens
#             view.name = name_screen
#             self.manager_screens.add_widget(view)
#
#
# vergel().run()
