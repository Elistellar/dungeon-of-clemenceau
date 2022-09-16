from pygame import Rect, Surface
from pygame.math import Vector2
from pygame.sprite import Sprite

from src.display.camera import Camera
from src.world.groups import UpdateGroup
from src.utils.consts import TILE_SIZE
from src.world.physics import Physics


class Entity(Sprite):
    
    CENTER_POS = Vector2(TILE_SIZE) / 2
    
    class speeds:
        WALK = 0.15
        RUN  = 0.25
    
    def __init__(self, pos: Vector2, sprite: Surface):
        super().__init__(Camera, UpdateGroup)
        
        self.pos = pos + self.CENTER_POS
        self.image = sprite
        self.rect = Rect(*self.pos, TILE_SIZE, TILE_SIZE)
        self.hitbox = self.rect.inflate(-14, -20)
    
        self.direction = Vector2()
        self.speed = self.speeds.WALK
    
    def update(self, dt: int):
        
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.pos.x += self.direction.x * dt * self.speed
        self.hitbox.x = self.pos.x
        Physics.collide_x(self)
        
        self.pos.y += self.direction.y * dt * self.speed
        self.hitbox.y = self.pos.y
        Physics.collide_y(self)
        
        self.rect.center = self.hitbox.center 
