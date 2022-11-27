from json import load, JSONDecodeError
from xml.etree.ElementTree import parse as XMLparse
from pathlib import Path

from pygame import Surface
from pygame.image import load as load_image
from pygame.mixer import Sound
from pygame.mixer import init as init_sound
from pygame.font import Font
from pygame.font import init as init_font

from src.utils.path import path
from src.world.tmx.region import Region
from src.world.tmx.tileset import Tileset


class Resource:
    
    PATH = "assets/assets.json"
    
    IMG_PATH = "assets/textures/"
    SPRITESHEET_PATH = "assets/spritesheets/"
    SOUNDS_PATH = "assets/sounds/"
    FONTS_PATH = "assets/fonts/"
    TMX_PATH = "assets/tmx/"
    
    @classmethod
    def load(cls):        
        try:
            with open(path(_p := cls.PATH), encoding="utf-8") as file:
                assets = load(file)
            
            cls.__images = {
                key: load_image(_p := path(cls.IMG_PATH + _path)).convert_alpha()
                for key, _path in assets["texture"].items()
            }
            
            cls.__spritesheet = {
                key: None
                for key, _path in assets["spritesheet"].items()
            }
            
            init_sound()
            cls.__sounds = {
                key: Sound(_p := path(cls.SOUNDS_PATH + _path))
                for key, _path in assets["sounds"].items()
            }
            
            init_font()
            cls.__fonts = {
                key: Font(cls.FONTS_PATH + (_p := data["file"]), data["size"])
                for key, data in assets["fonts"].items()
            }
            
            cls.__tilesets = {}
            cls.__tmx = {
                key: Region(
                    XMLparse(_p := path(cls.TMX_PATH + _path)).getroot(),
                    path(cls.TMX_PATH +_path).parent,
                    cls._load_tileset
                )
                for key, _path in assets["tmx"].items()
            }
            
        except (JSONDecodeError, ValueError):
            raise ValueError(f"Invalid file data : {_p}")
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Missing resource file : {_p}")
    
    @classmethod
    def _load_tileset(cls, path: Path) -> Tileset:
        if path not in cls.__tilesets:
            cls.__tilesets[path] = Tileset(path)
        
        return cls.__tilesets[path]
    
    @classmethod
    def img(cls, key: str) -> Surface:
        return cls.__images[key]
    
    @classmethod
    def spr(cls, key: str) -> None:
        raise NotImplementedError()
        return cls.__spritesheet[key]
    
    @classmethod
    def snd(cls, key: str) -> Sound:
        return cls.__sounds[key]
    
    @classmethod
    def fnt(cls, key: str) -> Font:
        return cls.__fonts[key]
    
    @classmethod
    def tmx(cls, key: str) -> Region:
        return cls.__tmx[key]
