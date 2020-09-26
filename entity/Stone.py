import arcade
import random

from entity.Entity import Entity

from graphics import Textures

class Stone(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.is_solid = True
        self.shake_count = 0
        self.shaking = False

        self.last_x = x
        self.last_y = y

        self.texture = Textures.SPRITESHEET_16[4 + 2 * 8]

        self.health = 20

    def update(self):

        if self.shake_count > 0:
            if self.shake_count % 2 == 0:
                self.center_x += random.random() - 0.5
                self.center_y += random.random() - 0.5
            else:
                self.center_x = self.last_x
                self.center_y = self.last_y

            self.shake_count -= 1

        elif self.shake_count == 0 and self.shaking:
            self.center_x = self.last_x
            self.center_y = self.last_y
            self.shaking = False

        super().update()

    def hurt(self, damage):
        self.shake_count = 6

        if not self.shaking:
            self.last_x = self.center_x
            self.last_y = self.center_y

        self.shaking = True

        self.health -= damage
        if self.health <= 0:
            self.die()