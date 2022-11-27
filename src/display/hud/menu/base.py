from __future__ import annotations

from typing import Tuple

from pygame import Surface
from pygame.locals import SRCALPHA

from src.display.hud.menu.components.component import Component
from src.display.window import Window
from src.events.event import Event
from src.events.queue import EventQueue as Events
from src.events.types import MENU_BACK
from src.sounds.sound import Sound
from src.utils.consts import COLOR_MENU_BACKGROUND, Orientation


class BaseMenu:
    
    BLACK_SURFACE = Surface(Window.Size.FULL_HD.value, SRCALPHA)
    BLACK_SURFACE.fill(COLOR_MENU_BACKGROUND)
    
    components: Tuple[Tuple[Component]] = tuple()
    submenus: dict[str, "BaseMenu"] = {}
    submenu: "BaseMenu" = None
    opened = False
    cursor: Tuple[int, int] = (None, None)

    @classmethod
    def escape(cls):
        if cls.submenu:
            cls.submenu.escape()
            if not cls.submenu.opened:
                cls.submenu = None
            
        else:
            for row in cls.components:
                for component in row:
                    if hasattr(component, "listening") and component.listening:
                        component.listening = False
                        Events.stop_listening()
                        return
                    
            cls.opened = False
    
    @classmethod
    def back(cls):
        Events.post(Event(MENU_BACK))
    
    @classmethod
    def open(cls):
        cls.opened = True
        
    @classmethod
    def open_sub(cls, name: str):
        cls.submenu = cls.submenus[name]
        cls.submenu.open()

    @classmethod
    def update(cls, dt: int):
        if cls.submenu:
            cls.submenu.update(dt)
        
        else:
            for y, row in enumerate(cls.components):
                for x, component in enumerate(row):
                    if component is None: continue
                    
                    if not Events.listening:
                        if component.rect.collidepoint(Events.cursor):
                            if not component.is_hovered:
                                Sound.play("button.hover", "menu")
                            component.is_hovered = True
                            cls.cursor = x, y
                            
                        if cls.cursor != (x, y):
                            component.is_hovered = False
                        
                    component.update(dt)

    @classmethod
    def render(cls):
        if cls.submenu:
            cls.submenu.render()
        else:
            Window.hud_surface.blit(
                cls.BLACK_SURFACE,
                (0, 0)
            )
            
            for row in cls.components:
                for component in row:
                    if component:
                        component.render()

    @classmethod
    def select_component(cls, direction: Orientation):
        if direction == Orientation.NORTH:
            if cls.cursor.y > 0:
                cls.cursor -= 1
                
        elif direction == Orientation.WEST:
            if cls.cursor.x > 0:
                cls.cursor.x -= 1
                
        elif direction == Orientation.SOUTH:
            if cls.cursor.y < len(cls.components) - 1:
                cls.cursor.y += 1
                
        elif direction == Orientation.EAST:
            if cls.cursor.x < len(cls.components[0]) - 1:
                cls.cursor.x += 1
