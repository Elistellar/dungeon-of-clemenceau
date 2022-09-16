from pygame import Surface
from pygame.image import load as load_img

from src.utils.path import path


class ResourcesLoader:
    
    IMG_DIR = "assets/textures/"
    imgs_names = {
        "player": "entities/player.png",
    }
    
    @classmethod
    def load(cls):
        cls.imgs = {
            key: load_img(path(cls.IMG_DIR + value)).convert_alpha()
            for key, value in cls.imgs_names.items()
        }
                
        cls.sounds = {
        }
    
    def __class_getitem__(cls, key: str) -> Surface:
        t, name = key.split(".")
        
        if t == "img":
            return cls.imgs[name]
        elif t == "sound":
            return cls.sounds[name]
        else:
            raise ValueError(f"Invalid resource type '{t}'")
