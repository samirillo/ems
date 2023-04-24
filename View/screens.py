# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.main_screen import MainScreenModel
from Model.new_screen import NewScreenModel
from Model.search_screen import SearchScreenModel
from Model.setting_screen import SettingScreenModel
from Model.update_screen import UpdateScreenModel

from Controller.main_screen import MainScreenController
from Controller.new_screen import NewScreenController
from Controller.search_screen import SearchScreenController
from Controller.setting_screen import SettingScreenController
from Controller.update_screen import UpdateScreenController

screens = {
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
