import arcade
import pyglet.gl as gl
import math

from graphics import Textures

from entity.EntityController import EntityController
from tiles import Tile
from level.LevelGen import LevelGen

PLAYER_MAX_SPEED = 80

class Level:

    def __init__(self, camera, mouse, keyboard):

        self.camera = camera
        self.mouse = mouse
        self.keyboard = keyboard

        self.width = 128
        self.height = 128

        self.tiles = [0] * self.width * self.height

        self.level_gen = LevelGen(self)

        self.level_gen.generate_level()

        self.sprite_list = arcade.SpriteList(use_spatial_hash=True)

        self.player = arcade.Sprite()
        self.player.texture = Textures.SPRITESHEET_16[0]
        self.player.center_x = self.width * 0.5 * Tile.TILE_SIZE
        self.player.center_y = self.height * 0.5 * Tile.TILE_SIZE

        self.sprite_list.append(self.player)

        self.tile_cursor = arcade.Sprite()
        self.tile_cursor.texture = Textures.get_texture(0, 4)
        self.tile_cursor.alpha = 128

        self.sprite_list.append(self.tile_cursor)

        self.physics_engine = arcade.PymunkPhysicsEngine(damping=0.4)

        self.physics_engine.add_sprite(self.player,
                               friction=1.0,
                               mass=4.0,
                               moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                               collision_type="player",
                               max_horizontal_velocity=PLAYER_MAX_SPEED,
                               max_vertical_velocity=PLAYER_MAX_SPEED)

        self.world_mouse = (0, 0)

        self.player_controller = EntityController(self.player, self.mouse, self.keyboard, self.physics_engine)

    def update(self, delta):
        
        self.player_controller.update()

        self.world_mouse = self.camera.screen_to_world_space(self.mouse.x, self.mouse.y)

        self.tile_cursor.left = int(self.world_mouse[0] / Tile.TILE_SIZE) * Tile.TILE_SIZE
        self.tile_cursor.bottom = int(self.world_mouse[1] / Tile.TILE_SIZE) * Tile.TILE_SIZE

        self.physics_engine.step()

        player_angle = math.degrees(math.atan2(
            self.world_mouse[1] - self.player.center_y,
            self.world_mouse[0] - self.player.center_x)
        )

        self.player.angle = player_angle

        # self.sprite_list.update()

        if self.keyboard.is_pressed("attack"):
            self.level_gen.offsetx = self.player.center_x / Tile.TILE_SIZE
            self.level_gen.offsety = self.player.center_y / Tile.TILE_SIZE
            self.level_gen.generate_level()

        self.camera.scroll_to(self.player.center_x, self.player.center_y)

    def draw(self):

        self.tile_sprite_list.draw(filter=gl.GL_NEAREST)
        self.sprite_list.draw(filter=gl.GL_NEAREST)

        # draw_start = self.camera.screen_to_world_space(0, 0)
        # draw_start = (int(draw_start[0] / 8), int(draw_start[1] / 8))

        # draw_end = self.camera.screen_to_world_space(self.camera.width, self.camera.height)
        # draw_end = (int(draw_end[0] / 8), int(draw_end[1] / 8))

        # for x in range(draw_start[0], draw_end[0]):
        #     for y in range(draw_start[1], draw_end[1]):
        #         tile = self.get_tile(x, y)

        #         if tile != 0:
        #             pass


    def get_tile(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return 0
        return self.tiles[x + y * self.width]