from pygame.math import Vector2

from src.actors.creature import Creature
from src.commanding.player_node import PlayerNode

#temporary for projectiles testing
from src.events.queue import EventQueue
from src.actors.projectile import Projectile
from src.display.window import Window
from src.items.container import Container


class Player(Creature):
    """
    The player sprite
    """
    
    SPRITE_SHEET_NAME = "balan_tmp"
    HITBOX = -14, -20
    
    
    def __init__(self, pos: Vector2):
        super().__init__(pos, 100)

        self.brain = PlayerNode()
        
        self.paused = False
        self.inventory = Container(6)

        #temporary for projectiles testing
        self.cooldown = 0

    def update(self, dt: int):
        
        if not self.paused:

            # performs standard entity actions
            super().update(dt)

            if self.cooldown>0:
                self.cooldown-=dt
                if self.cooldown<0:
                    self.cooldown=0

            if EventQueue.click_pressed and self.cooldown ==0:
                self.cooldown = 1000
                dir = EventQueue.cursor - Vector2(Window.size.value)*0.5
                print(dir)
                if dir.x==0 and dir.y==0:
                    dir = Vector2(1,0)
                Projectile(self.hitbox.center, dir, 300)
