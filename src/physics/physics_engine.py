from pygame import Rect
from pygame.math import Vector2

from src.data_storage.data_storage import DataStorage


class PhysicsEngine:
    """
    Computes all collisions
    """

    def amin(x: float, y: float):
        """
        return the value with lowest absolute value
        """
        return x if abs(x)<abs(y) else y

    def same_sign(x: float, y: float):
        """
        Return wether or not x and y have the same sign
        """
        return (x>0) == (x<0)

    def clip(direction: Vector2, origin: Rect):
        """
        clips the direction vector from the movment of the origin Rect
        considering all obstacles in the scene
        we are considering object are not overlaping
        returns the cliped vector
        """
        if direction.x ==0 and direction.y == 0: #if not moving, no clipping needs to be done
            return direction

        for obstacle in DataStorage.obstacles.sprites() + DataStorage.update.sprites():
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

    def all_on_line(origin: Vector2, direction: Vector2) -> list:
        """
        Returns the list of tuple containing body objects with hitbox 
        intersecting the half-line from origin point following direction 
        vector (this vector can have wathever magnitude). The second element
        of the tuple is the distance from origin point, considering the closest
        point of the hitbox from the origin point.
        Tuples are sorted by proximity from the center. 

        If direction vector is null vector, empty list is returned
        """

        if direction.x ==0 and direction.y == 0:
            return []

        result = []

        if direction.x == 0: #avoids zero-division
            for thing in DataStorage.obstacles.sprites() + DataStorage.update.sprites():
                target = thing.hitbox
                good_side = PhysicsEngine.same_sign(direction.y, target.center[1]-origin.y)

                if good_side and target.left<=origin.x and target.left+target.width>=origin.x:
                    result.append((thing, abs((target.top if direction.y>0 else target.top+target.height)-origin.y)))

        else:
            slope = direction.y/direction.x
            y_coord = lambda x: (x-origin.x) * slope + origin.y

            for thing in DataStorage.obstacles.sprites() + DataStorage.update.sprites():
                target = thing.hitbox
                if target.collidepoint(origin):
                    result.append(thing, 0)

                relative_pos = Vector2(target.center) - origin
                if relative_pos.dot(direction)>0: #if in the right direction
                    
                    left_point = (target.left, y_coord(target.left))
                    right_point= (target.left+target.width, y_coord(target.left+target.width))
                    clipped_line = target.clipline(left_point, right_point)

                    if clipped_line:
                        relative_pos = (Vector2(clipped_line[0]) if direction.x>0 else Vector2(clipped_line[1])) - origin
                        result.append((thing, relative_pos.magnitude()))

        #sorting on distance
        result.sort(key = lambda t: t[1])
        return result


    