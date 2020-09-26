import arcade

from tiles import Tile

from entity.Entity import Entity

class Mob(Entity):

    def __init__(self, x: float, y: float):
        super().__init__(x, y)

        self.curr_invis_frame = 0
        self.invis_frame = 12
        self.health = 5

        self.move_speed = 2

    def update(self):
        
        if self.curr_invis_frame > 0:
            self.curr_invis_frame -= 1
         
        if self.change_x != 0:
            self.move(self.change_x, 0)
        
        if self.change_y != 0:
            self.move(0, self.change_y)

        tile_x = int(self.center_x // Tile.TILE_SIZE)
        tile_y = int(self.center_y // Tile.TILE_SIZE)

        self.walked_on(tile_x, tile_y, self.level.get_tile(tile_x, tile_y))

    def move(self, dx: float, dy: float):
        
    # if dy != 0:
        self.center_y += dy

        # collision_list_y = self.level.get_tiles(
        #     int(self.left // TILE_SIZE),
        #     int(self.bottom // TILE_SIZE),
        #     int(self.right // TILE_SIZE),
        #     int(self.top // TILE_SIZE))

        # collision_list_y = arcade.check_for_collision_with_list(self, self.level.sprite_list)
        collision_list_y = self.level.sprite_list.spatial_hash.get_objects_for_box(self)

        for entity in collision_list_y:
            if not entity.is_solid:
                continue
            if self.intersects(entity):
                diff_x = self.center_x - entity.center_x - entity.change_x
                diff_y = self.center_y - entity.center_y - entity.change_y

                if abs(diff_x) > abs(diff_y):
                    continue

                if diff_y < 0:
                    self.center_y = entity.center_y - self.height_2 - entity.height_2
                elif diff_y > 0:
                    self.center_y = entity.center_y + self.height_2 + entity.height_2
                self.collided(entity, 0, dy)

    # if dx != 0:

        self.center_x += dx

        # collision_list_x = self.level.get_tiles(
        #     int(self.left // TILE_SIZE),
        #     int(self.bottom // TILE_SIZE),
        #     int(self.right // TILE_SIZE),
        #     int(self.top // TILE_SIZE))

        # collision_list_x = arcade.check_for_collision_with_list(self, self.level.sprite_list)
        collision_list_x = self.level.sprite_list.spatial_hash.get_objects_for_box(self)

        for entity in collision_list_x:
            if not entity.is_solid:
                continue
            if self.intersects(entity):
                diff_x = self.center_x - entity.center_x - entity.change_x
                diff_y = self.center_y - entity.center_y - entity.change_y

                if abs(diff_y) > abs(diff_x):
                    continue
                    
                if diff_x < 0:
                    self.center_x = entity.center_x - self.width_2 - entity.width_2
                elif diff_x > 0:
                    self.center_x = entity.center_x + self.width_2 + entity.width_2
                self.collided(entity, dx, 0)

    def attack(self):
        pass

    def walked_on(self, x, y, tile):
        pass

    def collided(self, entity, dx, dy):
        if dx != 0:
            self.change_x = 0
        if dy != 0:
            self.change_y = 0

    def hurt(self, damage):
        if self.curr_invis_frame <= 0:
            self.health -= damage
            self.curr_invis_frame = self.invis_frame

        if self.health <= 0:
            self.die()

    def heal(self, amount):
        self.health += amount

    def die(self):
        self.removed = True