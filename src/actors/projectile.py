from pygame.math import Vector2

from src.actors.entity import Entity
from src.commanding.projectile_node import ProjectileNode


class Projectile(Entity):
    """
    Represents an entity with HP value
    """

    SPRITE_SHEET_NAME = "proj_tmp"
    HITBOX = 0, 0

    def __init__(self, pos: Vector2, direction: Vector2):
        super().__init__(pos)
        
        self.brain = ProjectileNode(direction)
