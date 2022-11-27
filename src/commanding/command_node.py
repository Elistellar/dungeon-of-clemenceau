from pygame.math import Vector2


class CommandNode:
    """
    Base class for all command nodes
    """

    class speeds:
        WALK = 0.002
        SPRINT = 0.004

    def __init__(self):
        pass

    def get_direction() -> Vector2:
        return Vector2()
