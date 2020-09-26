import arcade
import pyglet.gl as gl

from graphics import Textures

class Inventory:

    def __init__(self):

        self.grid_size = 16
        self.grid_w = 4
        self.grid_h = 4

        self.gui_list = arcade.SpriteList()
        self.item_list = arcade.SpriteList()
        self.item_count = 0

        for x in range(self.grid_w):
            for y in range(self.grid_h):
                tile = arcade.Sprite()
                tile.texture = Textures.SPRITESHEET_16[24]
                tile.left = x * self.grid_size
                tile.bottom = y * self.grid_size
                self.gui_list.append(tile)

        self.add_item(1)

        self.add_item(0)
        self.add_item(3)
        self.add_item(3)
        self.add_item(5)

    def update(self):
        pass

    def draw(self):

        self.gui_list.draw(filter=gl.GL_NEAREST)
        self.item_list.draw(filter=gl.GL_NEAREST)

    def add_item(self, itemId):
        item_sprite = arcade.Sprite()
        item_sprite.texture = Textures.get_texture(itemId, 6)
        item_sprite.center_x = (self.item_count % self.grid_w) * self.grid_size + self.grid_size / 2
        item_sprite.center_y = (self.item_count // self.grid_w) * self.grid_size + self.grid_size / 2

        self.item_list.append(item_sprite)

        self.item_count += 1

    def remove_item(self, item):
        pass