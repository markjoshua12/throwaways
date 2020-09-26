import arcade
import random

from entity.Entity import Entity

from graphics import Textures

class Tree(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.is_solid = True
        self.shake_count = 0

        self.health = 20
        
        self.texture = Textures.SPRITESHEET_16[8]
        
        self.angle = random.randrange(0, 360)

    def update(self):

        if self.shake_count > 0:
            self.angle += random.randint(-4, 4)
            self.shake_count -= 1

        super().update()

    def hurt(self, damage):
        self.shake_count = 6
        self.health -= damage
        if self.health <= 0:
            self.die()