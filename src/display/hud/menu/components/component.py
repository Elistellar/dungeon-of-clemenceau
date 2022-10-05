from src.display.resource_loader import ResourceLoader


class Component:
    """
    A base class for all menu components.
    Handle all events required by subclasses.
    """
    
    @classmethod
    def init(cls):
        cls.font = ResourceLoader["font.main24"]
    
    mouse_pos: tuple[int, int]
    left_click: bool
    left_click_hold: bool
    keyup: int | None
    waiting_for_key = False
