from kivy.properties import StringProperty, ObjectProperty

from kivymd.uix.card import MDCard
from kivymd.uix.templates import StencilWidget


class StatCard(MDCard, StencilWidget):
    path_to_bg_image = StringProperty()
    stat_name = StringProperty()    
    view = ObjectProperty()

  