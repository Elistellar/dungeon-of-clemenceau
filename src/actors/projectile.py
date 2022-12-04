from pygame.math import Vector2

from src.actors.entity import Entity
from src.commanding.projectile_node import ProjectileNode
from src.utils.consts import PROJECTILE_BASE_HEIGHT


class Projectile(Entity):
    """
    Represents an entity with HP value
    """

    SPRITE_SHEET_NAME = "proj_tmp"
    HITBOX = 0, 0

    def __init__(self, pos: Vector2, direction: Vector2, reach: float):
        """
        pos: starting position of the projectile
        direction: the vector in 2D space the projectile is following
        reach: the lenght (in pixels), that the projectile must travel
        [is 100% accurate]
        """
        super().__init__(pos)
        
        self.brain = ProjectileNode(direction)
        self.life_time = 0
        self.max_time = reach/ProjectileNode.speeds.FLY

    def update(self, dt: int):

        # performs standard entity actions
        super().update(dt)
        self.rect = self.hitbox.move(0, (PROJECTILE_BASE_HEIGHT*((self.life_time/self.max_time)**2)) ) #animation of "falling"
        if self.collided or self.life_time>self.max_time:
            self.kill()
        self.life_time+=dt