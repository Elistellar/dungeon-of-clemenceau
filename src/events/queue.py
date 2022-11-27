from collections import deque

from pygame.event import get as pygame_event
from pygame.joystick import Joystick
from pygame.joystick import init as init_joystick
from pygame.key import get_pressed as get_keys_pressed
from pygame.locals import (JOYBUTTONUP, JOYDEVICEADDED, JOYDEVICEREMOVED,
                           K_ESCAPE, K_F3, K_F11, KEYUP, MOUSEBUTTONUP)
from pygame.locals import QUIT as P_QUIT
from pygame.math import Vector2
from pygame.mouse import get_pos as get_mouse_pos
from pygame.mouse import get_pressed as get_mouse_pressed

from src.events.event import Event
from src.events.types import (DEBUG, FULLSCREEN, MENU_BACK, MENU_MOVE_CURSOR,
                              MENU_PAUSE, QUIT)
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
    __joystick: Joystick = None
    listening = False
    pause_menu_opened = False
    
    __joystick_right_old = [0, 0]
    
    click: bool
    click_pressed: bool
    cursor: Vector2
    key_input: int = None
    
    __player_direction = Vector2()
    player_is_sprinting: bool
    
    @classmethod
    def init(cls):
        init_joystick()
    
    @classmethod
    def update(cls):
        cls.click = False
        cls.key_input = None
        
        if cls.listening:
            for event in pygame_event():
                if event.type == P_QUIT:
                    cls.post(Event(QUIT))
                    
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        cls.post(Event(MENU_BACK))
                    else:
                        cls.key_input = event.key
                        
                elif event.type == JOYBUTTONUP:
                    if event.button == 1:
                        cls.post(Event(MENU_BACK))
            return
        
        for event in pygame_event():
            t = event.type
            
            if t == P_QUIT:
                cls.post(Event(QUIT))
                
            elif t == KEYUP:                
                if event.key == K_F11:
                    cls.post(Event(FULLSCREEN))
                elif event.key == K_F3:
                    cls.post(Event(DEBUG))
                elif event.key == K_ESCAPE:
                    if cls.pause_menu_opened:
                        cls.post(Event(MENU_BACK))
                    else:
                        cls.post(Event(MENU_PAUSE))
            
            elif t == MOUSEBUTTONUP:
                cls.click = True
                
            elif t == JOYBUTTONUP:
                if event.button == 0:
                    cls.click = True
                elif event.button == 1:
                    cls.post(Event(MENU_BACK))
                elif event.button == 6:
                    if cls.pause_menu_opened:
                        cls.post(Event(MENU_BACK))
                    else:
                        cls.post(Event(MENU_PAUSE))
                
            elif t == JOYDEVICEADDED:
                cls.__joystick = Joystick(event.device_index)
            elif t == JOYDEVICEREMOVED:
                cls.__joystick = None
        
        # player movements
        keys = get_keys_pressed()
        cls.cursor = Vector2(get_mouse_pos())
        
        cls.__player_direction = Vector2()
        if keys[Settings["key.move_forward"]]:
            cls.__player_direction.y = -1
        elif keys[Settings["key.move_backward"]]:
            cls.__player_direction.y = 1
        elif cls.__joystick:
            val = cls.__joystick.get_axis(1) # vertical left
            if abs(val) > 0.1:
                cls.__player_direction.y = val
        
        if keys[Settings["key.move_left"]]:
            cls.__player_direction.x = -1
        elif keys[Settings["key.move_right"]]:
            cls.__player_direction.x = 1
        elif cls.__joystick:
            val = cls.__joystick.get_axis(0) # horizontal left
            if abs(val) > 0.1:
                cls.__player_direction.x = val
            
        cls.player_is_sprinting = keys[Settings["key.sprint"]]
        
        # menus
        mouse = get_mouse_pressed()
        cls.click_pressed = mouse[0]
        
        if cls.__joystick:
            x = cls.__joystick.get_axis(2) # horizontal right
            y = cls.__joystick.get_axis(3) # vertical right
            old_x, old_y = cls.__joystick_right_old
            
            SENSI = 0.2
            
            X, Y = 0, 0
            if old_x < SENSI and x > SENSI:
                X = 1
            elif old_x > -SENSI and x < -SENSI:
                X = -1
                
            elif old_y < SENSI and y > SENSI:
                Y = 1
            elif old_y > -SENSI and y < -SENSI:
                Y = -1
                
            if X or Y:
                cls.post(Event(MENU_MOVE_CURSOR, x=X, y=Y))            
            
            cls.__joystick_right_old[0] = x
            cls.__joystick_right_old[1] = y
    
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
    
    @classmethod
    def listen_for_key(cls):
        """
        Block almost all events, except QUIT and KEYUP, to allow user to change keybinds.
        """
        cls.listening = True
        
    @classmethod
    def stop_listening(cls):
        cls.listening = False
