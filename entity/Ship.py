import math

from tiles import Tile
from utils import Constants

from graphics import Textures

from entity.Entity import Entity
from entity.ShipPart import ShipPart

class Ship(Entity):

    def __init__(self, x, y, sprite_list):
        super().__init__(x, y)

        self.texture = Textures.get_texture(8, 8)

        self.tiles = {}
        self.sprite_list = sprite_list

    def update(self):

        if self.change_x == 0 and self.change_y == 0:
            return

        can_move = True

        self.center_x += self.change_x
        self.center_y += self.change_y

        tile_pos = (int((self.center_x - 4) // Tile.TILE_SIZE), int((self.center_y - 4) // Tile.TILE_SIZE))

        for pos, tile in self.tiles.items():

                tile_bl = self.level.get_tile(tile_pos[0] - pos[0], tile_pos[1] - pos[1]) != 0
                tile_br = self.level.get_tile(tile_pos[0] - pos[0] + 1, tile_pos[1] - pos[1]) != 0
                tile_tl = self.level.get_tile(tile_pos[0] - pos[0], tile_pos[1] - pos[1] + 1) != 0
                tile_tr = self.level.get_tile(tile_pos[0] - pos[0] + 1, tile_pos[1] - pos[1] + 1) != 0

                if tile_bl or tile_br or tile_tl or tile_tr:
                    can_move = False
                    break

        if not can_move:
            self.center_x -= self.change_x
            self.center_y -= self.change_y
            self.change_x = 0
            self.change_y = 0

    def add_tile(self, x, y, tileId, neighboring=True):

        pos_x = math.floor((self.center_x - x + 4) / Tile.TILE_SIZE)
        pos_y = math.floor((self.center_y - y + 4) / Tile.TILE_SIZE)

        tile_pos = (pos_x, pos_y)

        # if tile_pos in self.tiles:
        #     tile = self.tiles[tile_pos]

        #     diff_x = tile.center_x - x
        #     diff_y = tile.center_y - y

        #     new_pos_x = math.copysign(1, diff_x) + pos_x
        #     new_pos_y = math.copysign(1, diff_y) + pos_y

        #     if abs(diff_x) >= abs(diff_y):
        #         tile_pos = (pos_x, new_pos_y)
        #     else:
        #         tile_pos = (new_pos_x, pos_y)

        if tile_pos in self.tiles:
            return False

        has_neighbor = not neighboring
        for dir in Constants.DIRECTIONS:
            if (pos_x + dir[0], pos_y + dir[1]) in self.tiles:
                has_neighbor = True
                break

        if not has_neighbor:
            return False

        sprite = ShipPart(self, tile_pos[0], tile_pos[1], tileId)

        self.tiles[tile_pos] = sprite
        self.sprite_list.append(sprite)

        return True

    def remove_tile(self, x, y):

        pos_x = math.floor((self.center_x - x + 4) / Tile.TILE_SIZE)
        pos_y = math.floor((self.center_y - y + 4) / Tile.TILE_SIZE)

        tile_pos = (pos_x, pos_y)

        tile = self.tiles.pop(tile_pos, False)

        if tile:
            self.sprite_list.remove(tile)

        return tile

    # def intersects(self, entity):
    #     pass

