import math
import arcade
import random

from entity.Mob import Mob

from tiles import Tile

from graphics import Textures

class Goat(Mob):

    def __init__(self, x, y):

        super().__init__(x, y)

        self.move_speed = 1
        self.turn_speed = 12

        self.wander_time = 300
        self.curr_wander_time = 0

        self.stop_time = 120
        self.curr_stop_time = 0

        self.texture = Textures.SPRITESHEET_16[4 + 8]

        self.change_x = random.random() * self.move_speed
        self.change_y = random.random() * self.move_speed

        # self.is_solid = True

    def update(self):

        rand = random.random()

        is_water = self.level.get_tile(int(self.center_x // Tile.TILE_SIZE), int(self.center_y // Tile.TILE_SIZE)) == 0

        if self.curr_stop_time <= 0:
            self.stop()

        elif self.curr_wander_time <= 0 or is_water:
            if rand < 0.1:
                self.curr_stop_time = self.stop_time
            self.wander()
        else:
            self.curr_wander_time -= 1
            self.curr_stop_time -= 1

        super().update()

    def collided(self, entity, dx, dy):
        self.wander()
        # if dx != 0:
        #     self.change_x = 0
        # if dy != 0:
        #     self.change_y = 0

    def wander(self):
        rand = random.random()
        self.angle += self.turn_speed * rand

        self.change_x = math.cos(self.radians)
        self.change_y = math.sin(self.radians)

        self.curr_wander_time = self.wander_time * rand

    def stop(self):
        self.change_x = 0
        self.change_y = 0
        self.curr_stop_time = self.stop_time * random.random()