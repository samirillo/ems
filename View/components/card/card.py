from kivymd.uix.behaviors import RoundedRectangularElevationBehavior, HoverBehavior
from kivymd.theming import ThemableBehavior
from kivymd.uix.card import MDCard
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    NumericProperty,
    ObjectProperty,
    VariableListProperty,
    StringProperty
)

class Card(MDCard, RoundedRectangularElevationBehavior, ThemableBehavior, HoverBehavior):
    text = StringProperty()
    
    def on_enter(self, *args):
        '''The method will be called when the mouse cursor
        is within the borders of the current widget.'''

        #self.md_bg_color = self.theme_cls.primary_color

    def on_leave(self, *args):
        '''The method will be called when the mouse cursor goes beyond
        the borders of the current widget.'''

        #self.md_bg_color = self.theme_cls.bg_light