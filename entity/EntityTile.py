from entity.Entity import Entity

from graphics import Textures

class EntityTile(Entity):

    def __init__(self, x, y, tile):
        super().__init__(x, y)

        self.texture = Textures.get_texture(tile, 4)

        self.is_solid = True if tile >= 2 else False

    resource_price = [
        { "Stone": 0, "Wood": 5 },
        { "Stone": 0, "Wood": 5 },
        { "Stone": 0, "Wood": 10 },
        { "Stone": 0, "Wood": 5 }
    ]

    @staticmethod
    def get_resource_price(tile):
        pass