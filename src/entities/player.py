from pygame.key import get_pressed
from pygame.locals import K_d, K_q, K_s, K_z, K_LSHIFT
from pygame.math import Vector2

from src.display.resource_loader import ResourceLoader
from src.entities.entity import Entity
from src.settings import Settings


class Player(Entity):
    
    SPRITE_SHEET_NAME = "balan"
    
    HITBOX = -14, -20
    
    def __init__(self, pos: Vector2):
        super().__init__(pos, ResourceLoader["img.balan"])
        
        self.paused = False

    def update(self, dt: int):
        
        self.direction = Vector2()
        
        if not self.paused:
            keys = get_pressed()
            if keys[Settings["key.move_forward"]]:
                self.direction.y -= 1
            if keys[Settings["key.move_left"]]:
                self.direction.x -= 1
            if keys[Settings["key.move_backward"]]:
                self.direction.y += 1
            if keys[Settings["key.move_right"]]:
                self.direction.x += 1
                
            if keys[Settings["key.sprint"]]: # Sprint
                self.speed = self.speeds.SPRINT
            else:
                self.speed = self.speeds.WALK
                    
        super().update(dt)
