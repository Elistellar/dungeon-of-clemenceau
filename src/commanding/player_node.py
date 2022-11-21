
from pygame.math import Vector2
from pygame.event import Event
from pygame.event import KEYDOWN, KEYUP

from src.commanding.command_node import CommandNode
from src.events_controls.event_pipeline import EventQueue
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
        sprints = False
        #processing events
        while (not EventQueue.empty()):
            current = EventQueue.popEvent()

            if current.type == KEYDOWN:
                if current.key == Settings["key.move_forward"]:
                    direction.x = 1
                elif current.key == Settings["key.move_backward"]:
                    direction.x = 1
                elif current.key == Settings["key.move_left"]:
                    direction.y = -1
                elif current.key == Settings["key.move_right"]:
                    direction.y = 1
                elif current.key == Settings["key.sprint"]:
                    self.speed = self.speeds.SPRINT
            elif current.type == KEYUP:
                if current.key == Settings["key.sprint"]:
                    self.speed = self.speeds.WALK

        if direction.magnitude()!=0:
            return direction.normalize()*self.speed
        return direction
        
