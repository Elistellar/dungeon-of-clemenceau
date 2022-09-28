from pygame import Surface
from pygame.font import Font
from pygame.font import init as init_font
from pygame.image import load as load_img

from src.utils.path import path


class ResourceLoader:
    
    IMG_DIR = "assets/textures/"
    imgs_names = {
        "balan": "entities/balan.png",
    }
    
    animations = {}
    
    FONT_DIR = "assets/fonts/"
    fonts_data = {
        "main24": ("main.ttf", 24)
    }
    
    @classmethod
    def load(cls):
        cls.imgs = {
            key: load_img(path(cls.IMG_DIR + value)).convert_alpha()
            for key, value in cls.imgs_names.items()
        }
                
        cls.sounds = {
        }
        
        init_font()
        cls.fonts = {
            name: Font(path(cls.FONT_DIR + data[0]), data[1])
            for name, data in cls.fonts_data.items()
        }
    
    @classmethod
    def add_animation(cls, name: str, surfaces: dict[str, list[Surface]]):
        cls.animations[name] = surfaces
    
    def __class_getitem__(cls, key: str) -> Surface | dict[str, list[Surface]] | Font:
        t, name = key.split(".")
        
        if t == "img":
            return cls.imgs[name]
        elif t == "anim":
            return cls.animations[name]
        elif t == "sound":
            return cls.sounds[name]
        elif t == "font":
            return cls.fonts[name]
        else:
            raise ValueError(f"Invalid resource type '{t}'")
