from pygame import Rect, Surface
from pygame.math import Vector2
from pygame.sprite import Sprite

from src.display.camera import Camera
from src.display.sprite_sheet import SpriteSheet
from src.utils.consts import TILE_SIZE, Orientation
from src.world.groups import UpdateGroup
from src.world.physics import Physics


class Entity(Sprite):
    
    CENTER_POS = Vector2(TILE_SIZE) / 2
    
    # to overwite
    SPRITE_SHEET: dict[str, list[tuple[int, int]]]
    ANIMATION_SPEEDS: dict[str, int]
    
    HITBOX = 0, 0
    
    class speeds:
        WALK = 0.15
        SPRINT = 0.25
    
    class states:
        IDLEING   = "idle"
        WALKING   = "walk"
        SPRINTING = "sprint"
        ATTACKING = "attack"
    
    def __init__(self, pos: Vector2, sprite_sheet_surface: Surface):
        super().__init__(Camera, UpdateGroup)
        
        self.pos = pos + self.CENTER_POS
        self.rect = Rect(*self.pos, TILE_SIZE, TILE_SIZE)
        self.hitbox = self.rect.inflate(self.HITBOX)
        
        self.direction = Vector2()
        self.speed = self.speeds.WALK
        self.state = self.states.IDLEING
        self.orientation = Orientation.SOUTH
        
        self.sprite_sheet = SpriteSheet(sprite_sheet_surface, self.SPRITE_SHEET, self.ANIMATION_SPEEDS)
        self.sprite_sheet.change_animation(self.get_animation_name())
        self.image = self.sprite_sheet.get_surface()
    
    def get_animation_name(self) -> str:        
        return self.state + "." + self.orientation.value
    
    def update(self, dt: int):
        
        # State
        if self.direction.magnitude() == 0:
            self.state = self.states.IDLEING
        elif self.speed == self.speeds.WALK:
            self.state = self.states.WALKING
        elif self.speed == self.speeds.SPRINT:
            self.state = self.states.SPRINTING
            
        # Orientation
        if self.direction.x > 0:
            self.orientation = Orientation.EAST
        elif self.direction.x < 0:
            self.orientation = Orientation.WEST
            
        if self.direction.y > 0:
            self.orientation = Orientation.SOUTH
        elif self.direction.y < 0:
            self.orientation = Orientation.NORTH
        
        # Image
        animation_name = self.get_animation_name()
        if animation_name != self.sprite_sheet.animation_name:
            self.sprite_sheet.change_animation(animation_name)
        
        self.sprite_sheet.update(dt)
        self.image = self.sprite_sheet.get_surface()
        
        # Position
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.pos.x += self.direction.x * dt * self.speed
        self.hitbox.x = self.pos.x
        Physics.collide_x(self)
        
        self.pos.y += self.direction.y * dt * self.speed
        self.hitbox.y = self.pos.y
        Physics.collide_y(self)
        
        self.rect.center = self.hitbox.center 
