from collections import deque

from pygame.event import get as pygame_event
from pygame.key import get_pressed as get_keys_pressed
from pygame.locals import K_F3, K_F11, KEYUP
from pygame.locals import QUIT as P_QUIT
from pygame.math import Vector2

from src.events.event import Event
from src.events.types import DEBUG, FULLSCREEN, QUIT
from src.settings.settings import Settings


class EventQueueMeta(type):
    
    def __iter__(cls):
        return cls
    
    def __next__(cls):
        try:
            return cls._EventQueue__queue.popleft()
        except IndexError:
            raise StopIteration()

class EventQueue(metaclass=EventQueueMeta):
    
    __queue = deque()
    
    __player_direction = Vector2()
    player_is_sprinting: bool
    
    @classmethod
    def update(cls):
        for event in pygame_event():
            t = event.type
            
            if t == P_QUIT:
                cls.post(Event(QUIT))
                
            elif t == KEYUP:                
                if event.key == K_F11:
                    cls.post(Event(FULLSCREEN))
                if event.key == K_F3:
                    cls.post(Event(DEBUG))
                    
        keys = get_keys_pressed()
        
        cls.__player_direction = Vector2()
        if keys[Settings["key.move_forward"]]:
            cls.__player_direction.y = -1
        elif keys[Settings["key.move_backward"]]:
            cls.__player_direction.y = 1
        
        if keys[Settings["key.move_left"]]:
            cls.__player_direction.x = -1
        elif keys[Settings["key.move_right"]]:
            cls.__player_direction.x = 1
            
        cls.player_is_sprinting = keys[Settings["key.sprint"]]
    
    @classmethod
    def post(cls, event: Event):
        cls.__queue.append(event)
        
    @classmethod
    def get_player_direction(cls) -> Vector2:
        """
        Returns a Vector2 of lenght 1, pointing toward the direction player should look, according to user inputs 
        """
        if cls.__player_direction.magnitude() != 0:
            return cls.__player_direction.normalize()
        
        return cls.__player_direction
