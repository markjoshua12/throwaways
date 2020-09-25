import pymunk
import arcade

from graphics import Textures

from tiles import Tile

class ShipPart(arcade.Sprite):

    def __init__(self, ship, x, y, tile):
        super().__init__()

        self.texture = Textures.get_texture(tile, 4)

        self.ship = ship

        self.x = x
        self.y = y

        self.center_x = self.ship.center_x - self.x * Tile.TILE_SIZE
        self.center_y = self.ship.center_y - self.y * Tile.TILE_SIZE

    def update(self):
        self.center_x = self.ship.center_x - self.x * Tile.TILE_SIZE
        self.center_y = self.ship.center_y - self.y * Tile.TILE_SIZE

        super().update()
