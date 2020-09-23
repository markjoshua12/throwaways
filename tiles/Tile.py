from graphics import Textures

class Tile:

    def __init__(self, tileId, texture, solid=False):

        self.id = tileId
        self.texture = texture
        self.solid = solid

        TILES[tileId] = self

TILE_SIZE = 8

TILES = {}

WATER = Tile(0, Textures.get_texture(2, 0))
SAND = Tile(1, Textures.get_texture(0, 0))

WOOD = Tile(2, Textures.get_texture(4, 0))


TILE_EDGES = [(0, 1), (1, 0), (0, -1), (-1, 0)]
TILE_EDGE_COUNT = [1, 2, 4, 8]

TILE_EDGE_INDEX = [
    (0, 0), (1, 0), (1, 3), (2, 0),
    (1, 2), (3, 0), (2, 3), (4, 0),
    (1, 1), (2, 1), (3, 1), (4, 1),
    (2, 2), (4, 2), (4, 3), (5, 0)
]