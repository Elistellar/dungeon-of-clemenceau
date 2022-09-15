from pygame.math import Vector2
from pygame.key import get_pressed
from pygame.locals import K_z, K_q, K_s, K_d

from src.display.resources_loader import ResourcesLoader
from src.entities.entity import Entity


class Player(Entity):
    
    def __init__(self, pos: Vector2):
        super().__init__(pos, ResourcesLoader["img.player"])


    def update(self, dt: int):
        
        self.direction = Vector2()
        keys = get_pressed()
        if keys[K_z]: # Up
            self.direction.y -= 1
        if keys[K_q]: # Left
            self.direction.x -= 1
        if keys[K_s]: # Down
            self.direction.y += 1
        if keys[K_d]: # Right
            self.direction.x += 1
                    
        super().update(dt)