from pygame.key import get_pressed
from pygame.locals import K_d, K_q, K_s, K_z, K_LSHIFT
from pygame.math import Vector2

from src.display.resources_loader import ResourcesLoader
from src.entities.entity import Entity


class Player(Entity):
    
    SPRITE_SHEET = {
        "idle.north": [(1, 0)],
        "idle.south": [(0, 0)],
        "idle.east": [(2, 0)],
        "idle.west": [(3, 0)],
        "walk.north": [(1, 0), (1, 1), (1, 0), (1, 2)],
        "walk.south": [(0, 0), (0, 1), (0, 0), (0, 2)],
        "walk.east": [(2, 0), (2, 1), (2, 0), (2, 2)],
        "walk.west": [(3, 0), (3, 1), (3, 0), (3, 2)],
        "sprint.north": [(1, 0), (1, 1), (1, 0), (1, 2)],
        "sprint.south": [(0, 0), (0, 1), (0, 0), (0, 2)],
        "sprint.east": [(2, 0), (2, 1), (2, 0), (2, 2)],
        "sprint.west": [(3, 0), (3, 1), (3, 0), (3, 2)],
    }
    ANIMATION_SPEEDS = {        
        "idle.north": 1,
        "idle.south": 1,
        "idle.east": 1,
        "idle.west": 1,
        "walk.north": 0.15,
        "walk.south": 0.15,
        "walk.east": 0.15,
        "walk.west": 0.15,
        "sprint.north": 0.25,
        "sprint.south": 0.25,
        "sprint.east": 0.25,
        "sprint.west": 0.25,
    }
    
    HITBOX = -14, -20
    
    def __init__(self, pos: Vector2):
        super().__init__(pos, ResourcesLoader["img.balan"])

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
            
        if keys[K_LSHIFT]: # Sprint
            self.speed = self.speeds.SPRINT
        else:
            self.speed = self.speeds.WALK
                    
        super().update(dt)
