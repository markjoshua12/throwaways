import arcade

from graphics import Textures

class AnimatedSpriteManager:

    def __init__(self, tex_x, tex_y, tex_count):

        self.textures = []

        for i in range(tex_count):
            self.textures.append(Textures.get_texture_from_spritesheet(tex_x + i, tex_y, Textures.SPRITESHEET_16, 8, 8))

        self.current_index = 0

        self.frame_speed = 6
        self.frame_counter = 0

        self.frame_counter_len = self.frame_speed * len(self.textures)

        self.looping = True

    def update(self):

        self.frame_counter += 1

        if self.frame_counter >= self.frame_counter_len:
            self.frame_counter -= self.frame_counter_len

        self.current_index = self.frame_counter // self.frame_speed

    def get_texture(self):
        return self.textures[self.current_index]

    def reset(self):
        self.current_index = 0
        self.frame_counter = 0