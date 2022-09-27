from typing import Any

from pygame.event import post, Event
from pygame.locals import QUIT

from src.display.hud.menu.components.component import Component


class MetaMenu(type):
    
    def __getattribute__(self, __name: str) -> Any:
        if "open_" in __name:
            menu = self.submenues[__name.split("open_")[1]]
            menu.open()
        else:
            return super().__getattribute__(__name)

class Menu(metaclass=MetaMenu):
    
    submenues: dict[str, "Menu"] = {}
    components: list[Component]
    
    is_open = False
    
    @classmethod
    def open(cls):
        cls.is_open = True
    
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
                menu.update()
                return
            
        for component in cls.components:
            component.render()

    @classmethod
    def quit(cls):
        print(post(Event(
            QUIT
        )))
