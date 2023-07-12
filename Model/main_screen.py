from Model.base_model import BaseScreenModel
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.joinpath("assets", "data")


class MainScreenModel(BaseScreenModel):
    def __init__(self, database):
        self.database = database        
        self.stats_description = {}
        path_to_stats_description = DATA_DIR.joinpath(
            DATA_DIR, "stats-description.json"
        )
        if path_to_stats_description.exists():
            with open(path_to_stats_description) as json_file:
                self.stats_description = json.loads(json_file.read())
        self._observers = []

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)