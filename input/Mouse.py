

class Mouse:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        
        self.scroll_x = 0
        self.scroll_y = 0

        self.button = -1

        self.scrolling_count = 0

    def update(self):
        if self.scrolling_count:
            self.scrolling_count += 1
            if self.scrolling_count > 8:
                self.scroll_x = 0
                self.scroll_y = 0
                self.scrolling_count = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def on_mouse_press(self, x, y, button, modifiers):
        self.button = button

    def on_mouse_release(self, x, y, button, modifiers):
        self.button = 0

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.scroll_x = scroll_x
        self.scroll_y = scroll_y
        self.scrolling_count = 1