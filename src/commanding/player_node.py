from pygame.key import get_pressed
from pygame.math import Vector2

from src.commanding.command_node import CommandNode
from src.settings.settings import Settings


class PlayerNode(CommandNode):
    """
    The player's object brain.
    Interprates incomming events from the users and converts it into movements
    """

    def __init__(self):
        super().__init__()
        self.speed = self.speeds.WALK
        pass

    def getDirection(self)->Vector2:
        """
        Processes key inputs from the Event Queue to get a direction where to move
        """
        direction = Vector2(0,0)

        #processingkeys
        if get_pressed()[Settings["key.move_forward"]]:
            direction.y += -1
        if get_pressed()[Settings["key.move_backward"]]:
            direction.y += 1
        if get_pressed()[Settings["key.move_left"]]:
            direction.x += -1
        if get_pressed()[Settings["key.move_right"]]:
            direction.x += 1
        if get_pressed()[Settings["key.sprint"]]:
            self.speed = self.speeds.SPRINT
        else:
            self.speed = self.speeds.WALK

        if direction.magnitude()!=0:
            return direction.normalize()*self.speed
        return direction
        
