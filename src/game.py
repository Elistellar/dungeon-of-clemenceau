from pygame.event import get as get_events
from pygame.locals import QUIT, MOUSEBUTTONUP, KEYUP, K_ESCAPE
from pygame.math import Vector2
from pygame.time import Clock
from pygame.mouse import get_pos as get_mouse_pos

from src.display.camera import Camera
from src.display.resource_loader import ResourceLoader
from src.display.sprite_sheet import SpriteSheet
from src.display.window import Window
from src.entities.player import Player
from src.world.groups import UpdateGroup
from src.world.generator import LevelGenerator
from src.world.tmx.loader import TmxLoader
from src.display.hud.menu.components.component import Component
from src.display.hud.menu.escape import EscapeMenu


class Game:
        
    FRAMERATE = 60
    
    @classmethod
    def start(cls):
        # Initialization
        Window.create()
        ResourceLoader.load()
        SpriteSheet.load()
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
        
        cls.handle_events()
        
        UpdateGroup.update(dt)
        if EscapeMenu.is_open:
            EscapeMenu.update()
        
        cls.render()
    
    @classmethod
    def handle_events(cls):
        Component.left_click = False
        for event in get_events():
            
            if event.type == MOUSEBUTTONUP:
                if event.button == 0:
                    Component.left_click = True
                    
            elif event.type == KEYUP:
                if EscapeMenu.is_open:
                    EscapeMenu.close()
                    
                    if not EscapeMenu.is_open:
                        cls.player.paused = False
                else:
                    EscapeMenu.open()
                    cls.player.paused = True
                    
            elif event.type == QUIT:
                cls.quit()
                
        Component.mouse_pos = get_mouse_pos
    
    @classmethod
    def render(cls):
        Window.surface.fill((0, 0, 0))
        
        # level
        Camera.draw(cls.player)
        
        if EscapeMenu.is_open:
            EscapeMenu.render()
        
        Window.render()
    
    @classmethod
    def next_level(cls):
        cls.current_level = LevelGenerator.generate(cls.player)
    
    @classmethod
    def quit(cls):
        cls.running = False
        exit(0)
