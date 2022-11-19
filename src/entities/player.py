from pygame.key import get_pressed
from pygame.math import Vector2

from src.entities.entity import Entity
from src.items.container import Container
from src.settings.settings import Settings
from src.items.book import Book
from src.events_controls.mouse import Mouse


class Player(Entity):
    """
    The player sprite
    """
    
    SPRITE_SHEET_NAME = "balan"
    HITBOX = -14, -20
    
    def __init__(self, pos: Vector2):
        super().__init__(pos)
        
        self.paused = False
        self.inventory = Container(28)
        self.inventory.put(Book(self))

    def update(self, dt: int):
        
        self.direction = Vector2()
        
        if not self.paused:
            
            # Key inputs
            keys = get_pressed()
            if keys[Settings["key.move_forward"]]:
                self.direction.y -= 1
            if keys[Settings["key.move_left"]]:
                self.direction.x -= 1
            if keys[Settings["key.move_backward"]]:
                self.direction.y += 1
            if keys[Settings["key.move_right"]]:
                self.direction.x += 1
                
            if keys[Settings["key.sprint"]]:
                self.speed = self.speeds.SPRINT
            else:
                self.speed = self.speeds.WALK
            
            if Mouse.get_click(0):
                self.inventory.items[0].show(2)
                    
        super().update(dt)
