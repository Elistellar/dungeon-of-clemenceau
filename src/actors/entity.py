from enum import Enum

from pygame import Rect
from pygame.math import Vector2
from pygame.sprite import Sprite

from src.commanding.command_node import CommandNode
from src.data_storing.data_storage import DataStorage
from src.display.camera import Camera
from src.display.sprite_sheet import SpriteSheet
from src.physics.body import Body
from src.physics.physics_engine import PhysicsEngine
from src.utils.consts import TILE_SIZE, Orientation


class Entity(Sprite, Body):
    """
    A base class for all entities.
    """
    
    # to overwite
    SPRITE_SHEET_NAME: str

    class Kind(Enum):
        Abstract = 0
        Player = 1
    
    class states:
        IDLEING   = "idle"
        WALKING   = "walk"
        SPRINTING = "sprint"
        ATTACKING = "attack"
    
    def __init__(self, pos: Vector2):
        Sprite.__init__(self, Camera, DataStorage.entities)
        Body.__init__(self, Rect(*pos, TILE_SIZE, TILE_SIZE))
        
        self.direction = Vector2()
        self.brain = CommandNode()
            
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
        
        self.direction = self.brain.getDirection()
        
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
        PhysicsEngine.clip(self.direction, self.hitbox)
        self.hitbox.move(self.direction.x, self.direction.y)
        self.rect.center = self.hitbox.center 
