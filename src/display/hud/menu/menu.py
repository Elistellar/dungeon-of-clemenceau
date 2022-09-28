from typing import Any

from pygame.event import post, Event
from pygame.locals import QUIT

from src.display.hud.menu.components.component import Component


class Menu:
    
    submenues: dict[str, "Menu"] = {}
    components: list[Component]
    
    is_open = False
    
    @classmethod
    def open(cls):
        cls.is_open = True
    
    @classmethod
    def open_sub(cls, name: str):
        cls.submenues[name].open()
    
    @classmethod
    def close(cls):
        for menu in cls.submenues.values():
            if menu.is_open:
                menu.close()
                return
        
        cls.is_open = False
    
    @classmethod
    def update(cls):
        for menu in cls.submenues.values():
            if menu.is_open:
                menu.update()
                return
        
        for component in cls.components:
            component.update()
    
    @classmethod
    def render(cls):
        for menu in cls.submenues.values():
            if menu.is_open:
                menu.render()
                return
            
        for component in cls.components:
            component.render()

    @classmethod
    def quit(cls):
        post(Event(
            QUIT
        ))
