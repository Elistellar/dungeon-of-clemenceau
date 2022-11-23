from pygame import Rect


class Component:
    
    def __init__(self, rect: Rect):
        self.rect = rect
        self.is_hovered = False
