from entity.Entity import Entity

class Ship(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)

        self.tiles = {}

    def add_tile(self, x, y, tile):
        pos = (x, y)
        if self.tiles[pos]:
            return False

        self.tiles[pos] = tile