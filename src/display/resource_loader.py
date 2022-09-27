from pygame import Surface
from pygame.image import load as load_img

from src.utils.path import path


class ResourceLoader:
    
    IMG_DIR = "assets/textures/"
    imgs_names = {
        "balan": "entities/balan.png",
    }
    
    animations = {}
    
    @classmethod
    def load(cls):
        cls.imgs = {
            key: load_img(path(cls.IMG_DIR + value)).convert_alpha()
            for key, value in cls.imgs_names.items()
        }
                
        cls.sounds = {
        }
    
    @classmethod
    def add_animation(cls, name: str, surfaces: dict[str, list[Surface]]):
        cls.animations[name] = surfaces
    
    def __class_getitem__(cls, key: str) -> Surface | dict[str, list[Surface]]:
        t, name = key.split(".")
        
        if t == "img":
            return cls.imgs[name]
        elif t == "anim":
            return cls.animations[name]
        elif t == "sound":
            return cls.sounds[name]
        else:
            raise ValueError(f"Invalid resource type '{t}'")
