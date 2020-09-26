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

        self.debug = True

        if self.debug:
            import psutil
            import os

            self.frames = 0
            self.debug_time = 0

            self.debug_text = ""
            self.debug_text_list = TextList.create_text_list("Hello World!", 12, 12)

            self.process = psutil.Process(os.getpid())

    def on_update(self, delta):

        if self.keyboard.is_pressed("zoom_in") or self.mouse.scroll_y > 0:
            self.camera.zoom(0.98)
        elif self.keyboard.is_pressed("zoom_out") or self.mouse.scroll_y < 0:
            self.camera.zoom(1/0.98)

        self.level.update(delta)

        if self.debug:

            self.frames += 1
            self.debug_time += delta

            if self.debug_time >= 1:
                self.debug_text = f"FPS: {self.frames} | Using: {round(self.process.memory_info().rss / 1000000, 2)} MB"

                print(self.debug_text)

                TextList.empty_text_list(self.debug_text_list)
                TextList.add_to_text_list(self.debug_text, self.debug_text_list, 12, 12)
                
                self.debug_time -= 1
                self.frames = 0

        self.mouse.update()

    def on_draw(self):
        arcade.start_render()

        self.camera.set_viewport()

        self.level.draw()

        # self.camera.reset_viewport()
        self.set_viewport(0, self.width * 0.5, 0, self.height * 0.5)

        self.level.draw_gui()

        self.debug_text_list.draw(filter=gl.GL_NEAREST)

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