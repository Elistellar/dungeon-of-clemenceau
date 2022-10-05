from pygame import Rect
from pygame.math import Vector2
from pygame.sprite import Sprite

from src.display.camera import Camera
from src.display.sprite_sheet import SpriteSheet
from src.utils.consts import TILE_SIZE, Orientation
from src.world.groups import UpdateGroup
from src.world.physics import Physics


class Entity(Sprite):
    """
    A base class for all entities.
    """
    
    CENTER_POS = Vector2(TILE_SIZE) / 2
    
    # to overwite
    SPRITE_SHEET_NAME: str
    
    HITBOX = 0, 0
    
    class speeds:
        WALK = 0.15
        SPRINT = 0.25
    
    class states:
        IDLEING   = "idle"
        WALKING   = "walk"
        SPRINTING = "sprint"
        ATTACKING = "attack"
    
    def __init__(self, pos: Vector2):
        super().__init__(Camera, UpdateGroup)
        
        self.pos = pos + self.CENTER_POS
        self.direction = Vector2()
        self.speed = self.speeds.WALK
        
        self.rect = Rect(*self.pos, TILE_SIZE, TILE_SIZE)
        self.hitbox = self.rect.inflate(self.HITBOX)
            
        self.state = self.states.IDLEING
        self.orientation = Orientation.SOUTH
        
        self.sprite_sheet = SpriteSheet(self.SPRITE_SHEET_NAME)
        self.sprite_sheet.change_animation(self.get_animation_name())
        self.image = self.sprite_sheet.get_surface()
    
    def get_animation_name(self) -> str:        
        return self.state + "." + self.orientation.value
    
    def update(self, dt: int):
        """
        Update (in order) :
        - The state (IDELING, WALKING or SPRINTING)
        - The orientation (NORTH, ...)
        - The animation
        - The position
        """
        
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
