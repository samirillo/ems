from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.properties import ObjectProperty, StringProperty

class ScreenLayout(MDBoxLayout):
    title = StringProperty()
    nav_button = ObjectProperty()
    caption = StringProperty()

class GridContent(MDGridLayout): 
    pass