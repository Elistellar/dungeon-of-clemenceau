from pygame.display import flip
from pygame.event import get as get_events
from pygame.locals import QUIT
from pygame.math import Vector2
from pygame.time import Clock

from src.display.camera import Camera
from src.display.resources_loader import ResourcesLoader
from src.display.window import Window
from src.entities.player import Player
from src.entities.update_group import UpdateGroup
from src.world.generator import LevelGenerator
from src.world.tmx.loader import TmxLoader


class Game:
        
    FRAMERATE = 60
    
    @classmethod
    def start(cls):
        # Initialization
        Window.create()
        ResourcesLoader.load()
        TmxLoader.load()
        
        cls.running = True
        cls.clock = Clock()
        
        Camera.init()
        
        cls.player = Player(Vector2(0, 0))
        
        cls.next_level()
        
        while cls.running:
            cls.clock.tick(cls.FRAMERATE)
            cls.mainloop()
    
    @classmethod
    def mainloop(cls):
        dt = cls.clock.get_time()
        
        for event in get_events():
            if event.type == QUIT:
                cls.quit()
        
        UpdateGroup.update(dt)
        
        cls.render()
    
    @classmethod
    def render(cls):
        Window.surface.fill((0, 0, 0))
        
        # level
        Camera.draw(cls.player)
        
        flip()
    
    @classmethod
    def next_level(cls):
        cls.current_level = LevelGenerator.generate(cls.player)
    
    @classmethod
    def quit(cls):
        cls.running = False
        exit(0)
