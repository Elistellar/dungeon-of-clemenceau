from pygame.math import Vector2
from pygame import Rect

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
    