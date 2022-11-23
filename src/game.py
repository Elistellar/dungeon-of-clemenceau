from typing import NoReturn
import logging as log

from pygame.time import Clock
from pygame.math import Vector2

from src.events.queue import EventQueue
from src.display.window import Window
from src.events.types import QUIT, FULLSCREEN, DEBUG
from src.utils.consts import FRAMERATE, COLOR_BLACK, COLOR_BLACK_ALPHA
from src.world.level import Level
from src.actors.player import Player
from src.display.resource import Resource
from src.display.camera import Camera
from src.settings.settings import Settings
from src.data_storage.data_storage import DataStorage
from src.display.hud.debug import Debug


class GameEngine:
    
    @classmethod
    def init(cls):
        log.info("Loading game")
        Window.init(Window.Size.HD, Window.Size.HD)
        Window.set_title("Dungeon of Clemenceau")
        Resource.load()
        
        log.info("Loading settings")
        Settings.load()
        Debug.init()
        
        Camera.init()
        
        cls.player = Player(Vector2())
        cls.load_level(1)
        
        cls.clock = Clock()
    
    @classmethod
    def start(cls):
        cls.init()
        log.info("Let's go !")
        
        while True:
            cls.clock.tick(FRAMERATE)
            
            cls.handle_events()
            cls.update()
            cls.render()        
    
    @classmethod
    def handle_events(cls):
        EventQueue.update()
        
        for event in EventQueue:
            if event.type == QUIT:
                cls.quit()
                
            elif event.type == FULLSCREEN:
                Window.toggle_fullscreen()
                
            elif event.type == DEBUG:
                Debug.visible = not Debug.visible
                
    @classmethod
    def update(cls):
        dt = cls.clock.get_time()
        
        DataStorage.entities.update(dt)
        
        if Debug.visible:
            Debug.Infos.fps = round(cls.clock.get_fps())
    
    @classmethod
    def render(cls):
        Window.surface.fill(COLOR_BLACK)
        Window.hud_surface.fill(COLOR_BLACK_ALPHA)
        
        Camera.draw(cls.player)
        
        if Debug.visible:
            Debug.render()
               
        Window.render()
        
    @classmethod
    def load_level(cls, n: int):
        cls.map = Level(n, cls.player)
    
    @classmethod
    def quit(cls) -> NoReturn:
        exit(0)
