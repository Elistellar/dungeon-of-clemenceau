from pygame import Surface
from pygame.event import Event, post
from pygame.locals import QUIT, SRCALPHA

from src.display.hud.menu.components.component import Component
from src.display.window import Window
from src.utils.consts import WINDOW_SIZE


class Menu:
    """
    A base class for all menus.
    """
    
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
        """
        Open the 'name' submenue. It needs to be in the 'submenues' dict.
        """
        cls.submenues[name].open()
    
    @classmethod
    def close(cls):
        """
        Close a submenue if one is opened. Else, close this menu.
        """
        # Submenu
        for menu in cls.submenues.values():
            if menu.is_open:
                menu.close()
                return
        
        # This menu
        cls.is_open = False
    
    @classmethod
    def update(cls):
        """
        Update a submenue if one is opened. Else, update this menu.
        """
        # Submenu
        for menu in cls.submenues.values():
            if menu.is_open:
                menu.update()
                return
        
        # This menu
        for component in cls.components:
            component.update()
    
    @classmethod
    def render(cls):
        """
        Render a submenue if one is opened. Else, render this menu.
        """
        # Submenu
        for menu in cls.submenues.values():
            if menu.is_open:
                menu.render()
                return
        
        # This menu
        Window.hud_surface.blit(
            cls.background,
            (0, 0)
        )
        
        for component in cls.components:
            component.render()

    @classmethod
    def quit(cls):
        """
        Quit the game
        """
        post(Event(
            QUIT
        ))
