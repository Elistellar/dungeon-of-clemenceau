from pygame.locals import KEYDOWN, KEYUP
from pygame.math import Vector2

from src.commanding.command_node import CommandNode
from src.events.queue import EventQueue as Events
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

    def get_direction(self) -> Vector2:
        """
        Processes key inputs from the Event Queue to get a direction where to move
        """
        direction = Vector2(0,0)
        sprints = False
        # processing events                    
        if Events.player_is_sprinting:
            self.speed = self.speeds.SPRINT
        else:
            self.speed = self.speeds.WALK

        return Events.get_player_direction()
