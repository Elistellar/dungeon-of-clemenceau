from pygame.image import load as load_img
from pygame import Surface

from src.utils.path import path

class ResourcesLoader:
    
    TILE_SIZE = 32
    
    IMG_DIR = "assets/textures/"
    imgs_names = {
        "grass": "tileset/grass.png",
        "sand": "tileset/sand.png",
        "player": "entities/player.png",
    }
    
    @classmethod
    def load(cls):
        cls.imgs = {
            key: load_img(path(cls.IMG_DIR + value)).convert_alpha()
            for key, value in cls.imgs_names.items()
        }
        
        cls.tile_surfaces = [
            cls.imgs["grass"],
            cls.imgs["sand"],
        ]
        
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
