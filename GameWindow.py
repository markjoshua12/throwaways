import arcade
import pyglet.gl as gl
import random

from graphics.Camera import Camera
from graphics import TextList

from input.Keyboard import Keyboard
from input.Mouse import Mouse

from level.Level import Level

WIDTH = 1024
HEIGHT = 768
TITLE = "Throwaways"

class GameWindow(arcade.Window):

    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)

        arcade.set_background_color((84, 176, 207))

        self.center_window()

    def setup(self):
        
        self.camera = Camera(WIDTH, HEIGHT)
        self.camera.zoom(3/4)

        self.mouse = Mouse()
        self.keyboard = Keyboard()

        self.level = Level(self.camera, self.mouse, self.keyboard)

        self.debug_text = TextList.create_text_list("Hello World!", 4, 4)

    def on_update(self, delta):

        if self.keyboard.is_pressed("zoom_in"):
            self.camera.zoom(0.98)
        elif self.keyboard.is_pressed("zoom_out"):
            self.camera.zoom(1/0.98)

        self.level.update(delta)

    def on_draw(self):
        arcade.start_render()

        self.camera.set_viewport()

        self.level.draw()

        # self.camera.reset_viewport()
        self.set_viewport(0, self.width * 0.2, 0, self.height * 0.2)

        self.debug_text.draw(filter=gl.GL_NEAREST)

    def on_resize(self, width, height):
        self.camera.resize(width, height)


    def on_key_press(self, key, modifiers):
        self.keyboard.on_key_press(key, modifiers)

        if self.keyboard.is_pressed("fullscreen"):
            self.set_fullscreen(not self.fullscreen)
    
    def on_key_release(self, key, modifiers):
        self.keyboard.on_key_release(key, modifiers)


    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse.on_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        self.mouse.on_mouse_press(x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        self.mouse.on_mouse_release(x, y, button, modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.mouse.on_mouse_scroll(x, y, scroll_x, scroll_y)