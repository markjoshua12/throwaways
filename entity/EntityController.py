from entity.Entity import Entity
from input.Keyboard import Keyboard

class EntityController:

    def __init__(self, entity, mouse, keyboard):
        self.entity = entity
        self.mouse = mouse
        self.keyboard = keyboard
        # self.body = self.physics_engine.get_physics_object(self.entity).body;

        self.move_speed = 2

    def update(self):
        
        forceX = 0
        forceY = 0
        if self.keyboard.is_pressed("up"):
            self.entity.change_y = self.move_speed
        elif self.keyboard.is_pressed("down"):
            self.entity.change_y = -self.move_speed
        else:
            self.entity.change_y *= 0.8

        if self.keyboard.is_pressed("right"):
            self.entity.change_x = self.move_speed
        elif self.keyboard.is_pressed("left"):
            self.entity.change_x = -self.move_speed
        else:
            self.entity.change_x *= 0.8