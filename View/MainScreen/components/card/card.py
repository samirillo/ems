from kivy.properties import StringProperty, ObjectProperty

from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import StencilBehavior


class StatCard(MDCard, StencilBehavior):
    path_to_bg_image = StringProperty()
    stat_name = StringProperty()    
    view = ObjectProperty()

  