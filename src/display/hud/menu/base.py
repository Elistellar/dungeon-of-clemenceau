from __future__ import annotations

from typing import Tuple

from pygame import Surface
from pygame.locals import SRCALPHA
from pygame.math import Vector2

from src.display.hud.menu.components.component import Component
from src.display.hud.menu.components.slider import Slider
from src.display.window import Window
from src.events.event import Event
from src.events.queue import EventQueue as Events
from src.events.types import MENU_BACK
from src.sounds.sound import Sound
from src.utils.consts import COLOR_MENU_BACKGROUND


class BaseMenu:
    
    BLACK_SURFACE = Surface(Window.Size.FULL_HD.value, SRCALPHA)
    BLACK_SURFACE.fill(COLOR_MENU_BACKGROUND)
    
    components: Tuple[Tuple[Component]] = tuple()
    submenus: dict[str, "BaseMenu"] = {}
    submenu: "BaseMenu" = None
    opened = False
    cursor: Vector2

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
        cls.cursor = Vector2()
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
                        if component.rect.collidepoint(Events.cursor) or cls.cursor == Vector2(x, y):
                            if not component.is_hovered:
                                Sound.play("button.hover", "menu")
                            component.is_hovered = True
                            cls.cursor.x = x
                            cls.cursor.y = y
                            
                        if cls.cursor != Vector2(x, y):
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
    def select_component(cls, x: int, y: int):
        if cls.submenu:
            cls.submenu.select_component(x, y)
        else:       
            if y == 1: 
                if cls.cursor.y < len(cls.components) - 1:
                    cls.cursor.y += 1
            
            elif y == -1:
                if cls.cursor.y > 0:
                    cls.cursor.y -= 1
                    
            elif x == 1:
                if Events.click_pressed:
                    component = cls.components[int(cls.cursor.y)][int(cls.cursor.x)]
                    print(1)
                    if isinstance(component, Slider):
                        print(2)
                        component.cursor_rect.centerx += min(
                            component.rect.right - component.PADDINGX,
                            component.cursor_rect.centerx + 5
                        )
                        
                elif cls.cursor.x < len(cls.components[0]) - 1:
                    cls.cursor.x += 1
                    
            if x == -1:
                if Events.click_pressed:
                    print(3)
                    component = cls.components[int(cls.cursor.y)][int(cls.cursor.x)]
                    if isinstance(component, Slider):
                        print(4)
                        component.cursor_rect.centerx += max(
                            component.rect.left + component.PADDINGX,
                            component.cursor_rect.centerx - 5
                        )
                        
                elif cls.cursor.x > 0:
                    cls.cursor.x -= 1
                    
                    
            
