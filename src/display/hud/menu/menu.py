from pygame import Surface
from pygame.event import Event, post
from pygame.locals import QUIT, SRCALPHA

from src.display.hud.menu.components.component import Component
from src.display.window import Window
from src.utils.consts import WINDOW_SIZE


class Menu:
    
    submenues: dict[str, "Menu"] = {}
    components: list[Component]
    
    is_open = False
    background = Surface(WINDOW_SIZE, SRCALPHA)
    background.fill((0, 0, 0, 200))
    
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
        
        # Draw current menu
        Window.hud_surface.blit(
            cls.background,
            (0, 0)
        )
        
        for component in cls.components:
            component.render()

    @classmethod
    def quit(cls):
        post(Event(
            QUIT
        ))
