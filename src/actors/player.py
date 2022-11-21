from pygame.math import Vector2

from src.actors.entity import Entity
from src.commanding.player_node import PlayerNode
from src.events_controls.mouse import Mouse
from src.items.book import Book
from src.items.container import Container


class Player(Entity):
    """
    The player sprite
    """
    
    SPRITE_SHEET_NAME = "balan"
    HITBOX = -14, -20
    
    def __init__(self, pos: Vector2):
        super().__init__(pos)

        self.brain = PlayerNode() #custom brain
        
        self.paused = False
        self.inventory = Container(28)
        self.inventory.put(Book(self))

    def update(self, dt: int):
        
        if not self.paused:

            #performs standard entity actions
            super().update(dt)
            
            #others
            if Mouse.get_click(0):
                self.inventory.items[0].show(2)
