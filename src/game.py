from pygame.event import get as get_events
from pygame.locals import K_ESCAPE, KEYUP, MOUSEBUTTONUP, QUIT
from pygame.math import Vector2
from pygame.time import Clock

from src.display.camera import Camera
from src.display.hud.menu.components.component import Component
from src.display.hud.menu.escape import EscapeMenu
from src.display.hud.menu.loader import load_menus
from src.display.mouse import Mouse
from src.display.resource_loader import ResourceLoader
from src.display.sprite_sheet import SpriteSheet
from src.display.window import Window
from src.entities.player import Player
from src.lang import Lang
from src.settings import Settings
from src.sound import Sound
from src.world.generator import LevelGenerator
from src.world.groups import UpdateGroup
from src.world.tmx.loader import TmxLoader


class Game:
        
    FRAMERATE = 60
    
    @classmethod
    def start(cls):
        # Initialization        
        Window.create()
        
        Settings.load()
        
        ResourceLoader.load()
        SpriteSheet.load()
        Lang.load(Lang.Langs(Settings["lang"]))
        Component.init()
        TmxLoader.load()
        
        Sound.load()
        
        load_menus()
        
        # Declarations
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
            
            if not EscapeMenu.is_open:
                cls.player.paused = False
        
        cls.render()
    
    @classmethod
    def handle_events(cls):
        Component.keyup = None
        Component.left_click = False
        
        for event in get_events():
            
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    Component.left_click = True
                    
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    if EscapeMenu.is_open:
                        
                        if Component.waiting_for_key:
                            Component.waiting_for_key = False
                            
                        else:
                            EscapeMenu.close()
                            
                            if not EscapeMenu.is_open:
                                cls.player.paused = False
                    else:
                        EscapeMenu.open()
                        cls.player.paused = True
                else:
                    Component.keyup = event.key
                    
            elif event.type == QUIT:
                cls.quit()
                
        Component.mouse_pos = Mouse.get_pos()
        Component.left_click_hold = Mouse.get_pressed(0)
    
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
