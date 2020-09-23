from entity.Entity import Entity
from input.Keyboard import Keyboard

class EntityController:

    def __init__(self, entity, mouse, keyboard, physics_engine):
        self.entity = entity
        self.mouse = mouse
        self.keyboard = keyboard
        self.physics_engine = physics_engine

        self.body = self.physics_engine.get_physics_object(self.entity).body;

        self.move_speed = 1200

    def update(self):
        
        forceX = 0
        forceY = 0
        if self.keyboard.is_pressed("up"):
            forceY = self.move_speed
        elif self.keyboard.is_pressed("down"):
            forceY = -self.move_speed

        if self.keyboard.is_pressed("right"):
            forceX = self.move_speed
        elif self.keyboard.is_pressed("left"):
            forceX = -self.move_speed

        if forceX or forceY:
            self.body.apply_force_at_local_point((forceX, forceY), (0, 0))
        else:
            self.body.apply_impulse_at_local_point(-self.body.velocity * 0.8)