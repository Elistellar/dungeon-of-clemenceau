import logging as log
from typing import NoReturn

from pygame.math import Vector2
from pygame.time import Clock

from src.actors.player import Player
from src.data_storage.data_storage import DataStorage
from src.display.camera import Camera
from src.display.hud.debug import Debug
from src.display.hud.menu.achievements import AchievementsMenu
from src.display.hud.menu.components.component import Component
from src.display.hud.menu.controller import ControllerMenu
from src.display.hud.menu.display import DisplayMenu
from src.display.hud.menu.escape import EscapeMenu
from src.display.hud.menu.keybinds import KeybindsMenu
from src.display.hud.menu.language import LanguageMenu
from src.display.hud.menu.settings import SettingsMenu
from src.display.hud.menu.sound import SoundMenu
from src.display.resource import Resource
from src.display.window import Window
from src.events.queue import EventQueue
from src.events.types import DEBUG, FULLSCREEN, MENU_BACK, QUIT
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
        
        Camera.init()
        
        Sound.load()
        
        log.info("Loading menus")
        Component.init()
        
        EscapeMenu.quit = cls.quit
        EscapeMenu.init()
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
        
        DataStorage.update.update(dt)
        
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
        log.info("Bye !")
        exit(0)
