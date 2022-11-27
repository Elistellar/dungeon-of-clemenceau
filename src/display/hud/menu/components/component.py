from pygame import Rect

from src.display.resource import Resource


class Component:
    
    @classmethod
    def init(cls):
        cls.FONT = Resource.fnt("main24")
        
        cls.LARGE_BUTTON = Resource.img("menu.large_button")
        cls.LARGE_BUTTON_HOVERED = Resource.img("menu.large_button_hovered")
        
        cls.MEDIUM_BUTTON = Resource.img("menu.medium_button")
        cls.MEDIUM_BUTTON_HOVERED = Resource.img("menu.medium_button_hovered")
        
        cls.SMALL_BUTTON = Resource.img("menu.small_button")
        cls.SMALL_BUTTON_HOVERED = Resource.img("menu.small_button_hovered")
        
        cls.SLIDER_BAR = Resource.img("menu.slider_bar")
        cls.SLIDER_CURSOR = Resource.img("menu.slider_cursor")
    
    def __init__(self, rect: Rect):
        self.rect = rect
        self.is_hovered = False
