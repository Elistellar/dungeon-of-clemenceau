from src.display.resource_loader import ResourceLoader


class Component:
    
    @classmethod
    def init(cls):
        cls.font = ResourceLoader["font.main24"]
    
    mouse_pos: tuple[int, int]
    left_click: bool
