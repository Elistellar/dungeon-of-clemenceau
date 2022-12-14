import logging as log
from typing import NoReturn

from pygame.math import Vector2
from pygame.time import Clock

from src.achievements.achievement import Achievement
from src.achievements.triggers import get_item
from src.actors.player import Player
from src.data_storage.data_storage import DataStorage
from src.display.camera import Camera
from src.display.hud.debug import Debug
from src.display.hud.menu.achievements import AchievementsMenu
from src.display.hud.menu.components.component import Component
from src.display.hud.menu.controller import ControllerMenu
from src.display.hud.menu.display import DisplayMenu
from src.display.hud.menu.keybinds import KeybindsMenu
from src.display.hud.menu.language import LanguageMenu
from src.display.hud.menu.pause import PauseMenu
from src.display.hud.menu.settings import SettingsMenu
from src.display.hud.menu.sound import SoundMenu
from src.display.hud.notification import Notification
from src.display.resource import Resource
from src.display.window import Window
from src.events.queue import EventQueue
from src.events.types import (DEBUG, FULLSCREEN, MENU_BACK, MENU_MOVE_CURSOR,
                              MENU_PAUSE, QUIT)
from src.settings.lang import Lang
from src.settings.settings import Settings
from src.sounds.sound import Sound
from src.utils.consts import COLOR_BLACK, COLOR_BLACK_ALPHA, FRAMERATE
from src.world.level import Level


class GameEngine:
    
    @classmethod
    def init(cls):
        log.info("Loading game")
        Window.init(Window.Size.HD, Window.Size.HD)
        Window.set_title("Dungeon of Clemenceau")
        Resource.load()
        Window.set_icon(Resource.img("favicon"))
        
        log.info("Loading settings")
        Settings.load()
        Lang.load(Lang.Langs(Settings["lang"]))
        Debug.init()
        
        
        EventQueue.init()
        Camera.init()
        
        Sound.load()
        
        Notification.init()
        
        log.info("Loading achievements")
        # Achievement("book", lambda p: get_item(p, Arcsin))
        
        log.info("Loading menus")
        Component.init()
        
        PauseMenu.quit = cls.quit
        PauseMenu.init()
        AchievementsMenu.init()
        SettingsMenu.init()
        LanguageMenu.init()
        ControllerMenu.init()
        KeybindsMenu.init()
        SoundMenu.init()
        DisplayMenu.init()
        
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
        EventQueue.pause_menu_opened = PauseMenu.opened
        EventQueue.update()
        
        for event in EventQueue:
            if event.type == QUIT:
                cls.quit()
                
            elif event.type == FULLSCREEN:
                Window.toggle_fullscreen()
                
            elif event.type == DEBUG:
                Debug.visible = not Debug.visible
                Notification("achievement", "Test", 4)
                
            elif event.type == MENU_BACK:
                if PauseMenu.opened:
                    PauseMenu.escape()
            
            elif event.type == MENU_PAUSE:
                if not PauseMenu.opened:
                    PauseMenu.open()
                
            elif event.type == MENU_MOVE_CURSOR:
                if PauseMenu.opened:                    
                    PauseMenu.select_component(event.x, event.y)
                
    @classmethod
    def update(cls):
        dt = cls.clock.get_time()            
        
        DataStorage.update.update(dt)
        Notification.update(dt)
                
        if PauseMenu.opened:
            PauseMenu.update(dt)
        
        if Debug.visible:
            Debug.Infos.fps = round(cls.clock.get_fps())

    @classmethod
    def render(cls):
        Window.surface.fill(COLOR_BLACK)
        Window.hud_surface.fill(COLOR_BLACK_ALPHA)
        
        Camera.draw(cls.player)
        
        Notification.render()
        
        if PauseMenu.opened:
            PauseMenu.render()
        
        if Debug.visible:
            Debug.render()
               
        Window.render()
        
    @classmethod
    def load_level(cls, n: int):
        cls.map = Level(n, cls.player)
    
    @classmethod
    def quit(cls) -> NoReturn:
        log.info("Bye !")
        exit(0)
