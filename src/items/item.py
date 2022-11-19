from typing import TYPE_CHECKING

from pygame import Rect, Vector2
from pygame.sprite import Sprite

from src.display.camera import Camera
from src.display.sprite_sheet import SpriteSheet
from src.utils.consts import TILE_SIZE, Orientation
from src.world.groups import UpdateGroup
from src.utils.schedule import Schedule

if TYPE_CHECKING:
    from src.entities.entity import Entity


class Item(Sprite):
    
    name: str
    SPRITE_SHEET: str
    SHOW_DURATION = 0.6
        
    def __init__(self, owner: "Entity" = None):
        super().__init__()
        
        self.owner = owner
        self.visible = False
        
        self.rect = Rect(0, 0, TILE_SIZE, TILE_SIZE)
        
        self.sprite_sheet = SpriteSheet(self.SPRITE_SHEET)
        self.sprite_sheet.change_animation(self.get_animation_name())
        self.image = self.sprite_sheet.get_surface()
        
    def show(self, pos: Vector2 = None):
        if self.visible: return
        
        if self.owner:
            if self.owner.orientation == Orientation.NORTH:
                self.rect.centerx = self.owner.hitbox.centerx
                self.rect.bottom = self.owner.hitbox.top
            elif self.owner.orientation == Orientation.SOUTH:
                self.rect.centerx = self.owner.hitbox.centerx
                self.rect.top = self.owner.hitbox.bottom
            elif self.owner.orientation == Orientation.EAST:
                self.rect.centery = self.owner.hitbox.centery
                self.rect.left = self.owner.hitbox.right
            else:
                self.rect.centery = self.owner.hitbox.centery
                self.rect.right = self.owner.hitbox.left
        else:
            self.rect.center = pos
            
        Camera.add(self)
        UpdateGroup.add(self)
        self.visible = True
        self.update_animation(0)
        
        if self.SHOW_DURATION is not None:
            Schedule.post(self.SHOW_DURATION, self.hide)
        
    def hide(self):
        Camera.remove(self)
        UpdateGroup.remove(self)
        self.visible = False
        
    def update(self, dt: int):
        """
        Update (in order) :
        - The position
        - The animation
        """        
            
        # Position
        if self.visible and self.owner:
            if self.owner.orientation == Orientation.NORTH:
                self.rect.centerx = self.owner.hitbox.centerx
                self.rect.bottom = self.owner.hitbox.top
            elif self.owner.orientation == Orientation.SOUTH:
                self.rect.centerx = self.owner.hitbox.centerx
                self.rect.top = self.owner.hitbox.bottom
            elif self.owner.orientation == Orientation.EAST:
                self.rect.centery = self.owner.hitbox.centery
                self.rect.left = self.owner.hitbox.right
            else:
                self.rect.centery = self.owner.hitbox.centery
                self.rect.right = self.owner.hitbox.left
                
        # Image
        self.update_animation(dt)
    
    def update_animation(self, dt: int):
        animation_name = self.get_animation_name()
        if animation_name != self.sprite_sheet.animation_name:
            self.sprite_sheet.change_animation(animation_name)
        
        self.sprite_sheet.update(dt)
        self.image = self.sprite_sheet.get_surface()

    def get_animation_name(self):
        return self.owner.orientation.value
