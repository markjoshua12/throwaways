import math
import arcade

from entity.Mob import Mob
from entity.ShipPart import ShipPart

from graphics import Textures
from graphics.AnimatedSpriteManager import AnimatedSpriteManager

class Player(Mob):

    def __init__(self, x, y):

        super().__init__(x, y)

        self.move_speed = 1

        self.swimming = False

        self.texture = Textures.SPRITESHEET_16[0]

        self.walk_anim = AnimatedSpriteManager(0, 0, 4)
        self.water_walk_anim = AnimatedSpriteManager(4, 0, 4)
        self.curr_anim = self.walk_anim

    def update(self):

        if self.swimming:
            self.move_speed = 0.5
            self.curr_anim = self.water_walk_anim
        else:
            self.curr_anim = self.walk_anim
            self.move_speed = 1

        if abs(self.change_x) > 0.2 or abs(self.change_y) > 0.2:
            self.curr_anim.update()
            self.texture = self.curr_anim.get_texture()
        elif self.swimming:
            self.texture = Textures.SPRITESHEET_16[4]
        else:
            self.texture = Textures.SPRITESHEET_16[0]

        super().update()

        touched_list = self.level.sprite_list.spatial_hash.get_objects_for_point(self.position)

        for entity in touched_list:
            if not self.intersects(entity):
                continue
            if isinstance(entity, ShipPart):
                self.swimming = False
                if abs(self.change_x) < 0.5:
                    self.change_x += entity.ship.change_x - self.change_x
                if abs(self.change_y) < 0.5:
                    self.change_y += entity.ship.change_y - self.change_y
                break

    def attack(self):

        attack_dir_x = math.sin(self.radians) * self.width_2
        attack_dir_y = math.cos(self.radians) * self.height_2

        self.center_x += attack_dir_x
        self.center_y += attack_dir_y

        hit_list = arcade.check_for_collision_with_list(self, self.level.sprite_list)

        for entity in hit_list:
            entity.hurt(1)

        self.center_x -= attack_dir_x
        self.center_y -= attack_dir_y

    def walked_on(self, x, y, tile):

        if tile == 0:
            # self.texture = Textures.SPRITESHEET_16[3]
            self.swimming = True
        else:
            # self.texture = Textures.SPRITESHEET_16[0]
            self.swimming = False