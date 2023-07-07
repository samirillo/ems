import os

from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty

from View.base_screen import BaseScreenView
from Utility.observer import Observer
from View.MainScreen.components.card.card import StatCard


class MainScreenView(BaseScreenView):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()
    parallax_step = NumericProperty(50)

    _cursor_pos_x = 0

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def on_enter(self):
        self.ids.carousel.clear_widgets()
        self.generate_and_added_slides_to_carousel()

    def generate_and_added_slides_to_carousel(self):
        for stat_name in self.model.stats_description.keys():
            card = StatCard(
                path_to_bg_image=os.path.join(
                    "assets", "images", f"{stat_name}.png"
                ),
                stat_name=stat_name.capitalize(),
                view=self,
            )
            self.ids.carousel.add_widget(card)

    def do_animation_card_content(self, instance_carousel, offset_value):
        direction = self.get_direction_swipe(offset_value)
        self._cursor_pos_x = offset_value
        offset_value = max(min(abs(offset_value) / Window.width, 1), 0)

        for instance_slide in [
            instance_carousel.current_slide,
            instance_carousel.next_slide,
            instance_carousel.previous_slide
        ]:
            if instance_slide:
                if direction == "left":
                    instance_slide.ids.image_bg.x -= offset_value
                elif direction == "right":
                    instance_slide.ids.image_bg.x += offset_value

    def get_direction_swipe(self, offset_value):
        if self._cursor_pos_x > offset_value:
            direction = "left"
        else:
            direction = "right"
        return direction

    def model_is_changed(self, option) -> None:
        pass