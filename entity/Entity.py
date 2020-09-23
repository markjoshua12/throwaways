import arcade

class Entity(arcade.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.center_x = x
        self.center_y = y

    def intersects_rect(self, x, y, width, height):

        # dist_x = (self.center_x - x+width/2)**2
        # dist_y = (self.center_y - y+height/2)**2

        # col_radius = (self.collision_radius + max(width, height))

        # if dist_x + dist_y > col_radius * col_radius:
        #     return False

        left_x = max(self.x, x)
        bottom_y = max(self.y, y)
        right_x = min(self.x + self.width, x + width)
        top_y = min(self.y + self.height, y + height)

        return left_x < right_x and bottom_y < top_y