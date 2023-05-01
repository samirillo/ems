# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.splash_screen import SplashScreenModel
from Model.login_screen import LoginScreenModel
from Model.singup_screen import SingupScreenModel
from Model.main_screen import MainScreenModel
from Model.new_screen import NewScreenModel
from Model.search_screen import SearchScreenModel
from Model.setting_screen import SettingScreenModel
from Model.update_screen import UpdateScreenModel

from Controller.splash_screen import SplashScreenController
from Controller.login_screen import LoginScreenController
from Controller.singup_screen import SingupScreenController
from Controller.main_screen import MainScreenController
from Controller.new_screen import NewScreenController
from Controller.search_screen import SearchScreenController
from Controller.setting_screen import SettingScreenController
from Controller.update_screen import UpdateScreenController

screens = {
    "splash screen": {
        "model": SplashScreenModel,
        "controller": SplashScreenController,
    },

    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },

    "singup screen": {
        "model": SingupScreenModel,
        "controller": SingupScreenController,
    },
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
    "new screen": {
        "model": NewScreenModel,
        "controller": NewScreenController,
    },
    "search screen": {
        "model": SearchScreenModel,
        "controller": SearchScreenController,
    },    
    "setting screen": {
        "model": SettingScreenModel,
        "controller": SettingScreenController,
    },  
    "update screen": {
        "model": UpdateScreenModel,
        "controller": UpdateScreenController,
    },         
}
