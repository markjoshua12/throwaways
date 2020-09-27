import arcade
import pyglet.gl as gl
import math
import random

from graphics import Textures
from graphics import TextList

from entity.EntityController import EntityController
from entity.Ship import Ship
from entity.Entity import Entity
from entity.Mob import Mob
from entity.Player import Player
from entity.Shark import Shark
from entity.EntityTile import EntityTile

from tiles import Tile
from level.LevelGen import LevelGen

from item.Inventory import Inventory

PLAYER_MAX_SPEED = 80

class Level:

    def __init__(self, camera, mouse, keyboard):

        self.camera = camera
        self.mouse = mouse
        self.keyboard = keyboard

        self.width = 256
        self.height = 256

        self.tiles = [0] * self.width * self.height
        self.tiles_top = [0] * self.width * self.height

        self.sprite_list = arcade.SpriteList(use_spatial_hash=True, spatial_hash_cell_size=32)
        self.ship_list = arcade.SpriteList(use_spatial_hash=True)
        self.effect_list = arcade.SpriteList()
        self.tile_sprite_list = None

        self.gui_list = arcade.SpriteList()
        self.health_list = arcade.SpriteList()

        self.player = Player(self.width * 0.5 * Tile.TILE_SIZE, self.height * 0.5 * Tile.TILE_SIZE)
        self.player.level = self

        self.sprite_list.append(self.player)

        self.level_gen = LevelGen(self)

        self.level_gen.generate_level()

        self.tile_cursor = arcade.Sprite()
        self.tile_cursor.texture = Textures.get_texture(0, 4)
        self.tile_cursor.alpha = 128

        self.effect_list.append(self.tile_cursor)

        self.ship = Ship(self.player.center_x + 32, self.player.center_y, self.ship_list)
        self.ship.level = self
        self.ship.change_x = -0.2
        # self.ship.change_y = -0.2

        self.ship.add_tile(self.ship.center_x, self.ship.center_y, 4, False)
        self.ship.add_tile(self.ship.center_x + 8, self.ship.center_y, 0, False)
        self.ship.add_tile(self.ship.center_x + 8, self.ship.center_y + 8, 0, False)
        self.ship.add_tile(self.ship.center_x, self.ship.center_y + 8, 1, False)

        self.sprite_list.append(self.ship)

        self.tile_type = 0
        self.tool_type = 0

        self.world_mouse = (0, 0)

        self.player_controller = EntityController(self.player, self.mouse, self.keyboard)

        self.inventory = Inventory()

        self.effect_list.append(self.player)

        self.game_over = False
        self.game_over_text = TextList.create_text_list("Game Over!", self.camera.width // 4, self.camera.height // 4, bold=True, centered=True)

        for i in range(3):
            tool_sprite = arcade.Sprite()
            tool_sprite.texture = Textures.SPRITESHEET_16[i + 3 * 8]
            tool_sprite.center_x = self.camera.width // 4 + i * 16 - 16
            tool_sprite.bottom = 4

            self.gui_list.append(tool_sprite)

        self.tool_tips = ["Oar", "Build Blocks", "Build Ship"]
        self.tool_tips_list = TextList.create_text_list(self.tool_tips[self.tool_type], self.camera.width // 4, 24, centered=True)

        self.tool_selected = arcade.Sprite()
        self.tool_selected.texture = Textures.SPRITESHEET_16[3 + 3 * 8]
        self.tool_selected.center_x = self.camera.width // 4 + self.tool_type * 16 - 16
        self.tool_selected.bottom = 4

        self.gui_list.append(self.tool_selected)

        for i in range(self.player.health):
            heart = arcade.Sprite()
            heart.texture = Textures.get_texture(0, 8)
            heart.left = 4 + i * 9
            heart.top = self.camera.height * 0.5 - 4

            self.health_list.append(heart)

    def update(self, delta):
        
        self.player_controller.update()

        self.world_mouse = self.camera.screen_to_world_space(self.mouse.x, self.mouse.y)

        for i in range(1, 8):
            if self.keyboard.is_pressed(str(i)):
                self.tile_type = i - 1
                self.tile_cursor.texture = Textures.get_texture(self.tile_type, 4)
                break

        if self.player.health <= 0:
            self.game_over = True

        for i in range(len(self.health_list)):
            if (i >= self.player.health):
                self.health_list[i].alpha = 0
            else:
                self.health_list[i].alpha = 255

        player_angle = math.atan2(
            self.world_mouse[1] - self.player.center_y,
            self.world_mouse[0] - self.player.center_x)

        self.player.radians = player_angle

        tile_x = int(self.world_mouse[0] // Tile.TILE_SIZE)
        tile_y = int(self.world_mouse[1] // Tile.TILE_SIZE)

        if self.tool_type == 1:
            self.tile_cursor.center_x = tile_x * Tile.TILE_SIZE + 4
            self.tile_cursor.center_y = tile_y * Tile.TILE_SIZE + 4
        if self.tool_type == 2:
            self.tile_cursor.center_x = self.ship.center_x - math.floor((self.ship.center_x - self.world_mouse[0] + 4) / Tile.TILE_SIZE) * Tile.TILE_SIZE
            self.tile_cursor.center_y = self.ship.center_y - math.floor((self.ship.center_y - self.world_mouse[1] + 4) / Tile.TILE_SIZE) * Tile.TILE_SIZE

        if self.mouse.button == 1:
            changed_tool = False
            for i in range(3):
                if self.gui_list[i].collides_with_point((self.mouse.x * 0.5, self.mouse.y * 0.5)):
                    self.tool_type = i

                    self.tool_selected.center_x = self.camera.width // 4 + self.tool_type * 16 - 16
                    self.tool_selected.bottom = 4

                    TextList.empty_text_list(self.tool_tips_list)
                    TextList.add_to_text_list(self.tool_tips[self.tool_type],
                        self.tool_tips_list, self.camera.width // 4, 24,
                        centered=True)

                    changed_tool = True
                    break

            if not changed_tool:
                if self.tool_type == 0:
                    self.ship.change_x += (math.cos(player_angle) - self.ship.change_x) * 0.4
                    self.ship.change_y += (math.sin(player_angle) - self.ship.change_y) * 0.4

                elif self.tool_type == 1:
                    if self.get_tile(tile_x, tile_y) < 3:
                        tile = EntityTile(self.tile_cursor.center_x, self.tile_cursor.center_y, self.tile_type)
                        tile.level = self

                        self.tiles_top[tile_x + tile_y * self.width] = 5 + self.tile_type
                        self.sprite_list.append(tile)

                elif self.tool_type == 2:
                    self.ship.add_tile(self.world_mouse[0], self.world_mouse[1], self.tile_type)

        elif self.mouse.button == 4:
            if self.tool_type == 0:
                self.ship.change_x *= 0.95
                self.ship.change_y *= 0.95

            elif self.tool_type == 1:
                self.tiles_top[tile_x + tile_y * self.width] = 0

            elif self.tool_type == 2:
                self.ship.remove_tile(self.world_mouse[0], self.world_mouse[1])

        for entity in self.sprite_list:
            if entity.removed:
                self.sprite_list.remove(entity)
                continue

            entity.update()


        self.ship_list.update()

        # if self.keyboard.is_pressed("attack"):
        #     self.level_gen.offsetx = self.player.center_x / Tile.TILE_SIZE
        #     self.level_gen.offsety = self.player.center_y / Tile.TILE_SIZE
        #     self.level_gen.generate_level()

        self.camera.scroll_to(self.player.center_x, self.player.center_y)

    def draw(self):

        self.tile_sprite_list.draw(filter=gl.GL_NEAREST)
        self.ship_list.draw(filter=gl.GL_NEAREST)
        self.sprite_list.draw(filter=gl.GL_NEAREST)
        self.effect_list.draw(filter=gl.GL_NEAREST)

        # draw_start = self.camera.screen_to_world_space(0, 0)
        # draw_start = (int(draw_start[0] / 8), int(draw_start[1] / 8))

        # draw_end = self.camera.screen_to_world_space(self.camera.width, self.camera.height)
        # draw_end = (int(draw_end[0] / 8), int(draw_end[1] / 8))

        # for x in range(draw_start[0], draw_end[0]):
        #     for y in range(draw_start[1], draw_end[1]):
        #         tile = self.get_tile(x, y)

        #         if tile != 0:
        #             pass

    def draw_gui(self):
        self.gui_list.draw(filter=gl.GL_NEAREST)
        self.health_list.draw(filter=gl.GL_NEAREST)

        if self.game_over:
            self.game_over_text.draw(filter=gl.GL_NEAREST)
        # self.inventory.draw()

        self.tool_tips_list.draw(filter=gl.GL_NEAREST)

    def add_entity(self, entity, list):
        entity.level = self

        list.append(entity)

    def get_tile(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return 0
        idx = x + y * self.width

        return self.tiles_top[idx] if self.tiles_top[idx] else self.tiles[idx]