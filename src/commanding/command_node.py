from pygame.math import Vector2


class CommandNode:
    """
    Base class for all command nodes
    """

    class speeds:
        WALK = 0.15
        SPRINT = 0.25

    def __init__(self):
        pass

    def getDirection()->Vector2:
        return Vector2()
