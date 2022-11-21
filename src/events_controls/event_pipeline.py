from pygame.event import Event
from pygame.event import poll
from pygame.event import get as get_events
from pygame.locals import K_ESCAPE, K_F3, KEYUP, KEYDOWN, MOUSEBUTTONUP, QUIT
from enum import Enum

from src.game import GameEngine
from src.events_controls.mouse import Mouse
from src.display.hud.menu.components.component import Component
from src.display.hud.menu.escape import EscapeMenu
from src.display.hud.debug import Debug


class SpecialEvent(Enum):
    EXIT=0
    ESCAPE=1
    DBG=2

class EventQueue:
    """
    Class handeling incomming events from user.
    """

    def popEvent(cls):
        """
        returns first event
        """
        return cls.queue.pop(0)

    def empty(cls)->bool:
        """
        Indicates wether there is still events in the queue or not
        """
        return cls.queue == []

    def collect(cls):
        """
        Collects all events of the frame and pre-processes it
        also returns a list of codes for special events that has to 
        """
        special_ones = []
        cls.queue = []
        currentEvent = poll()
        for event in get_events():
            
            if event.type == MOUSEBUTTONUP:
                Mouse.btns[event.button-1] = True
                if event.button == 1:
                    Component.left_click = True
                    
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    special_ones.append(SpecialEvent.ESCAPE)

                elif event.key == K_F3:
                    special_ones.append(SpecialEvent.DBG)
                
                else:
                    cls.queue.append(currentEvent)
                    Component.keyup = event.key

            elif event.type == KEYDOWN:
                cls.queue.append(currentEvent)

            elif event.type == QUIT:
               special_ones.append(SpecialEvent.EXIT)

        return special_ones