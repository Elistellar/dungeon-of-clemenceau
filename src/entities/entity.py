from pygame import Rect, Surface
from pygame.math import Vector2
from pygame.sprite import Sprite

from src.display.camera import Camera
from src.entities.update_group import UpdateGroup
from src.utils.consts import TILE_SIZE


class Entity(Sprite):
    
    CENTER_POS = Vector2(TILE_SIZE) / 2
    
    def __init__(self, pos: Vector2, sprite: Surface):
        super().__init__(Camera, UpdateGroup)
        
        self.pos = pos + self.CENTER_POS
        self.image = sprite
        self.rect = Rect(*self.pos, TILE_SIZE, TILE_SIZE)
    
        self.direction = Vector2()
        self.speed = 0.3
    
    def update(self, dt: int):
        
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.pos.x += self.direction.x * dt * self.speed
        self.pos.y += self.direction.y * dt * self.speed        

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
