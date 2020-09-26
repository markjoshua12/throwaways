import arcade

import Maths

from tiles import Tile

class Entity(arcade.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.center_x = x
        self.center_y = y

        self.is_solid = False
        self.level = None

        self.width = Tile.TILE_SIZE
        self.height = Tile.TILE_SIZE

        self.width_2 = self.width / 2
        self.height_2 = self.height / 2

        self.health = 5
        self.removed = False

    def create_hit_box(self, width, height):
        self.set_hit_box(Maths.create_hit_box(width, height))

    def intersects(self, entity):
        left_x = max(self.center_x - self.width_2, entity.center_x - self.width_2)
        bottom_y = max(self.center_y - self.height_2, entity.center_y - self.height_2)
        right_x = min(self.center_x + self.width_2, entity.center_x + self.width_2)
        top_y = min(self.center_y + self.height_2, entity.center_y + self.height_2)

        return left_x < right_x and bottom_y < top_y

        # return intersects_rect(entity.left, entity.bottom, entity.width, entity.height)

    def intersects_rect(self, x, y, width, height):

        # dist_x = (self.center_x - x+width/2)**2
        # dist_y = (self.center_y - y+height/2)**2

        # col_radius = (self.collision_radius + max(width, height))

        # if dist_x + dist_y > col_radius * col_radius:
        #     return False

        left = max(self.left, x)
        bottom = max(self.bottom, y)
        right = min(self.right, x + width)
        top = min(self.top, y + height)

        return left < right and bottom < top

    def hurt(self, damage):
        pass

    def die(self):
        self.removed = True