import math

from entity.Entity import Entity
from input.Keyboard import Keyboard

class EntityController:

    def __init__(self, entity, mouse, keyboard):
        self.entity = entity
        self.mouse = mouse
        self.keyboard = keyboard

        self.move_speed = 2

    def update(self):
        
        if self.keyboard.is_pressed("up"):
            self.entity.change_y = self.entity.move_speed
        elif self.keyboard.is_pressed("down"):
            self.entity.change_y = -self.entity.move_speed
        else:
            self.entity.change_y *= 0.8

        if self.keyboard.is_pressed("right"):
            self.entity.change_x = self.entity.move_speed
        elif self.keyboard.is_pressed("left"):
            self.entity.change_x = -self.entity.move_speed
        else:
            self.entity.change_x *= 0.8

        if self.keyboard.is_pressed("e"):

            self.entity.attack()