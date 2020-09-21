import arcade

from level.Level import Level

WIDTH = 1024
HEIGHT = 768
TITLE = "Throwaway"

class GameWindow(arcade.Window):

    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)

        arcade.set_background_color((25, 12, 5))

        self.center_window();

    def setup(self):
        pass

    def on_update(self, delta):
        pass

    def on_draw(self):
        arcade.start_render()