from pygame.math import Vector2

from src.commanding.command_node import CommandNode


class ProjectileNode(CommandNode):
    """
    Represents a projectile
    """

    def __init__(self, direction: Vector2):
        super().__init__()
        self.dir = direction.normalize()

    def get_direction(self) -> Vector2:
        """
        Processes key inputs from the Event Queue to get a direction where to move
        """      
        return self.dir