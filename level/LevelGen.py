import arcade
import noise

from graphics import Textures

from tiles import Tile


class LevelGen:

    def __init__(self, level):
        self.level = level;

        self.width = level.width
        self.height = level.height

        self.octaves = 4
        self.freq = 1.0 / (16.0 * self.octaves)
        self.freq2 = 1.0 / (2.0 * self.octaves)

        self.repeatx = self.width
        self.repeaty = self.height

        self.offsetx = 0
        self.offsety = 0

    def generate_level(self):

        self.level.tile_sprite_list = arcade.SpriteList()

        for x in range(self.width):
            for y in range(self.height):
                tile_noise = noise.pnoise2((x + self.offsetx) * self.freq, (y + self.offsety) * self.freq,
                                            self.octaves,
                                            repeatx=self.repeatx, repeaty=self.repeaty)
                tile_noise2 = noise.pnoise2((x + self.offsetx) * self.freq2, (y + self.offsety) * self.freq2,
                                            self.octaves,
                                            repeatx=self.repeatx, repeaty=self.repeaty) + 0.6
                tile_noise *= tile_noise2

                if tile_noise < .08:
                    self.level.tiles[x + y * self.width] = 0
                elif tile_noise < (.1 + tile_noise2 * 0.1):
                    self.level.tiles[x + y * self.width] = 1
                else:
                    self.level.tiles[x + y * self.width] = 2

        for x in range(self.width):
            for y in range(self.height):
                tileId = self.level.tiles[x + y * self.width]

                if tileId != 0:

                    edgeByte = 0
                    
                    for i, edge in enumerate(Tile.TILE_EDGES):
                        if self.level.get_tile(x + edge[0], y + edge[1]) >= tileId:
                            edgeByte += Tile.TILE_EDGE_COUNT[i]

                    edgeIdx = Tile.TILE_EDGE_INDEX[edgeByte]

                    tileSprite = arcade.Sprite()

                    tileSprite.texture = Textures.get_texture(5 - edgeIdx[0], tileId) #Tile.TILES[tileId].texture
                    tileSprite.angle = 90 * edgeIdx[1]
                    tileSprite.left = x * Tile.TILE_SIZE
                    tileSprite.bottom = y * Tile.TILE_SIZE

                    self.level.tile_sprite_list.append(tileSprite)