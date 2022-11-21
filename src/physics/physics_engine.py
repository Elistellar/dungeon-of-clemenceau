from pygame import Rect
from pygame.math import Vector2


class PhysicsEngine:
    """
    Computes all collisions
    """

    def clip(cls, direction: Vector2, origin: Rect):
        """
        clips the direction vector from the movment of the origin Rect
        considering all physical body in the scene
        """
        return direction
    