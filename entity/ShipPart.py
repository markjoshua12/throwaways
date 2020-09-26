import pymunk
import arcade

from graphics import Textures

from entity.Entity import Entity

from tiles import Tile

class ShipPart(Entity):

    def __init__(self, ship, x, y, tile):
        super().__init__(0, 0)

        self.texture = Textures.get_texture(tile, 4)

        self.ship = ship

        self.x = x
        self.y = y

        self.center_x = self.ship.center_x - self.x * Tile.TILE_SIZE
        self.center_y = self.ship.center_y - self.y * Tile.TILE_SIZE

        self.is_solid = True if tile >= 2 else False

    def update(self):
        self.center_x = self.ship.center_x - self.x * Tile.TILE_SIZE
        self.center_y = self.ship.center_y - self.y * Tile.TILE_SIZE

        super().update()
