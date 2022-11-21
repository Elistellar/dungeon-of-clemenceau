import logging as log

from pygame.math import Vector2
from pygame.time import Clock

from src.actors.player import Player
from src.data_storing.data_storage import DataStorage
from src.display.camera import Camera
from src.display.hud.debug import Debug
from src.display.hud.menu.components.component import Component
from src.display.hud.menu.escape import EscapeMenu
from src.display.hud.menu.loader import load_menus
from src.display.resource_loader import ResourceLoader
from src.display.sprite_sheet import SpriteSheet
from src.display.window import Window
from src.events_controls.event_pipeline import EventQueue, SpecialEvent
from src.events_controls.mouse import Mouse
from src.settings.lang import Lang
from src.settings.settings import Settings
from src.sounds.sound import Sound
from src.utils.consts import FRAMERATE
from src.utils.schedule import Schedule
from src.world.generator import LevelGenerator
from src.world.tmx.loader import TmxLoader


class GameEngine:
    """
    The main game class, where the loop stands.
    """
    
    @classmethod
    def start(cls):
        cls.load()

        cls.running = True
        cls.clock = Clock()
        
        Camera.init()
        
        cls.player = Player(Vector2(0, 0))
        
        cls.next_level()
        
        while cls.running:
            cls.clock.tick(FRAMERATE)
            cls.mainloop()
            
    @classmethod
    def load(cls):
        log.info("Loading game")
        Window.create()
        
        log.info("Loading settings")
        Settings.load()
        Sound.load()
        
        log.info("Loading resources :")
        ResourceLoader.load()
        SpriteSheet.load()
        TmxLoader.load()
        Lang.load(Lang.Langs(Settings["lang"]))
        
        log.info("Loading menus")
        Component.init()
        load_menus()
        Debug.init()
    
    @classmethod
    def mainloop(cls):
        dt = cls.clock.get_time()
        Debug.Infos.fps = round(cls.clock.get_fps())
        
        cls.handle_events()

        Schedule.update()
        DataStorage.updateActors(dt)
        if EscapeMenu.is_open:
            EscapeMenu.update()
            
            if not EscapeMenu.is_open:
                cls.player.paused = False
        
        cls.render()
    
    @classmethod
    def handle_events(cls):
        Mouse.btns = [
            False, False, False
        ]
        
        Component.keyup = None
        Component.left_click = False

        to_consider = EventQueue.collect()
        
        for event in to_consider:
                    
            if event == SpecialEvent.ESCAPE:
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

            elif event == SpecialEvent.DBG:
                Debug.visible = not Debug.visible
                    
            elif event == SpecialEvent.EXIT:
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
            
        if Debug.visible:
            Debug.render()
        
        Window.render()
    
    @classmethod
    def next_level(cls):
        cls.current_level = LevelGenerator.generate(cls.player)
    
    @classmethod
    def quit(cls):
        cls.running = False
        log.info("Closing game")
        exit(0)
