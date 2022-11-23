import logging as log
from typing import NoReturn

from pygame.math import Vector2
from pygame.time import Clock

from src.actors.player import Player
from src.data_storage.data_storage import DataStorage
from src.display.camera import Camera
from src.display.hud.debug import Debug
from src.display.hud.menu.achievements import AchievementsMenu
from src.display.hud.menu.components.large_button import LargeButton
from src.display.hud.menu.components.small_button import SmallButton
from src.display.hud.menu.escape import EscapeMenu
from src.display.hud.menu.language import LanguageMenu
from src.display.hud.menu.options import OptionsMenu
from src.display.resource import Resource
from src.display.window import Window
from src.events.queue import EventQueue
from src.events.types import DEBUG, FULLSCREEN, MENU_BACK, QUIT
from src.settings.lang import Lang
from src.settings.settings import Settings
from src.utils.consts import COLOR_BLACK, COLOR_BLACK_ALPHA, FRAMERATE
from src.world.level import Level


class GameEngine:
    
    @classmethod
    def init(cls):
        log.info("Loading game")
        Window.init(Window.Size.HD, Window.Size.HD)
        Window.set_title("Dungeon of Clemenceau")
        Resource.load()
        
        log.info("Loading settings")
        Settings.load()
        Lang.load(Lang.Langs(Settings["lang"]))
        Debug.init()
        
        Camera.init()
        
        log.info("Loading menus")
        SmallButton.init()
        LargeButton.init()
        
        EscapeMenu.init()
        AchievementsMenu.init()
        OptionsMenu.init()
        LanguageMenu.init()
        
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
                
            elif event.type == MENU_BACK:
                if EscapeMenu.opened:
                    EscapeMenu.escape()
                else:
                    EscapeMenu.open()
                
    @classmethod
    def update(cls):
        dt = cls.clock.get_time()
        
        DataStorage.entities.update(dt)
        
        if EscapeMenu.opened:
            EscapeMenu.update(dt)
        
        if Debug.visible:
            Debug.Infos.fps = round(cls.clock.get_fps())
    
    @classmethod
    def render(cls):
        Window.surface.fill(COLOR_BLACK)
        Window.hud_surface.fill(COLOR_BLACK_ALPHA)
        
        Camera.draw(cls.player)
        
        if EscapeMenu.opened:
            EscapeMenu.render()
        
        if Debug.visible:
            Debug.render()
               
        Window.render()
        
    @classmethod
    def load_level(cls, n: int):
        cls.map = Level(n, cls.player)
    
    @classmethod
    def quit(cls) -> NoReturn:
        exit(0)
