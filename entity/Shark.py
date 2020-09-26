import math
import arcade

from entity.Mob import Mob

class Shark(Mob):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.target = None
        self.target_delay = 0
        self.curr_target_delay = self.target_delay

        self.angle_rad = 0
        self.move_speed = 0.5

    def update(self):

        if self.target is None:
            self.look_for_target()
        elif self.curr_target_delay <= 0:
            diff_x = self.target.center_x - self.center_x
            diff_y = self.target.center_y - self.center_y

            self.angle_rad = math.atan2(diff_y, diff_x)

            self.change_x = math.cos(self.angle_rad) * self.move_speed
            self.change_y = math.sin(self.angle_rad) * self.move_speed

            self.radians = self.angle_rad

            self.curr_target_delay = self.target_delay
        else:
            self.curr_target_delay -= 1

        super().update()

    def look_for_target(self):

        for entity in self.level.sprite_list:
            if entity != self and isinstance(entity, Mob):
                self.target = entity
                break

    def walked_on(self, x, y, tile):
        if tile != 0:
            self.center_x -= self.change_x
            self.center_y -= self.change_y
