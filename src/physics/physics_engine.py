from pygame import Rect
from pygame.math import Vector2

from src.data_storage.data_storage import DataStorage


class PhysicsEngine:
    """
    Computes all collisions
    """

    def amin(x, y):
        """
        return the value with lowest absolute value
        """
        return x if abs(x)<abs(y) else y

    @classmethod
    def clip(cls, direction: Vector2, origin: Rect):
        """
        clips the direction vector from the movment of the origin Rect
        considering all obstacles in the scene
        we are considering object are not overlaping
        """
        for obstacle in DataStorage.obstacles.sprites():
            target = obstacle.hitbox
            centers = (Vector2(origin.center), Vector2(target.center))
            relative_pos = centers[1] - centers[0]

            if direction.dot(relative_pos)>0: #we only consider object in the direction that we are facing (and if we are moving)
                minimal_vector= Vector2()
                minimal_vector.x =  (origin.width+target.width)*0.5*(-1 if relative_pos.x<0 else 1)
                minimal_vector.y = (origin.height+target.height)*0.5*(-1 if relative_pos.y<0 else 1)

                if abs(relative_pos.x)<abs(minimal_vector.x): #collision on y (one is just above the other)
                    direction.y = PhysicsEngine.amin(direction.y, relative_pos.y - minimal_vector.y)
                elif abs(relative_pos.y)<abs(minimal_vector.y): #collision on x (one is to the left of the other)
                    direction.x = PhysicsEngine.amin(direction.x, relative_pos.x - minimal_vector.x)

        return direction
    