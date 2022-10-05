from pygame import Surface
from pygame.font import Font
from pygame.font import init as init_fonts
from pygame.image import load as load_img
from pygame.mixer import Sound
from pygame.mixer import init as init_sounds

from src.utils.path import path


class ResourceLoader:
    """
    Handle all resources to not load them several times.
    """
    
    IMG_DIR = "assets/textures/"
    imgs_names = {
        "balan": "entities/balan.png",
    }
    
    animations = {}
    
    SOUND_DIR = "assets/sounds/"
    sounds_names = {
        "btn_hover": "btn_hover.mp3",
        "btn_click": "btn_click.mp3",
    }
    
    FONT_DIR = "assets/fonts/"
    fonts_data = {
        "main24": ("main.ttf", 24),
    }
    
    @classmethod
    def load(cls):
        cls.imgs = {
            name: load_img(path(cls.IMG_DIR + value)).convert_alpha()
            for name, value in cls.imgs_names.items()
        }
        
        init_sounds()
        cls.sounds = {
            name: Sound(path(cls.SOUND_DIR + value))
            for name, value in cls.sounds_names.items()
        }
        
        init_fonts()
        cls.fonts = {
            name: Font(path(cls.FONT_DIR + data[0]), data[1])
            for name, data in cls.fonts_data.items()
        }
    
    @classmethod
    def add_animation(cls, name: str, surfaces: dict[str, list[Surface]]):
        cls.animations[name] = surfaces
    
    def __class_getitem__(cls, key: str) -> Surface | dict[str, list[Surface]] | Sound | Font:
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
