from entity.Entity import Entity
from input.Keyboard import Keyboard

class EntityController:

    def __init__(self, entity, mouse, keyboard):
        self.entity = entity
        self.mouse = mouse
        self.keyboard = keyboard

        self.move_speed = 3

    def update(self):
        
        if self.keyboard.is_pressed("up"):
            self.entity.change_y = self.move_speed
        elif self.keyboard.is_pressed("down"):
            self.entity.change_y = -self.move_speed
        else:
            self.entity.change_y = 0

        if self.keyboard.is_pressed("right"):
            self.entity.change_x = self.move_speed
        elif self.keyboard.is_pressed("left"):
            self.entity.change_x = -self.move_speed
        else:
            self.entity.change_x = 0

