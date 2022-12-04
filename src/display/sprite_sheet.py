import logging as log

from pygame import Surface
from pygame.locals import SRCALPHA

from src.utils.consts import TILE_SIZE
from src.display.resource import Resource


class SpriteSheet:
    """
    Handle the animation of a sprite.
    """
    
    FRAMES = {
        "balan": {
            "idle.north": [(1, 0)],
            "idle.south": [(0, 0)],
            "idle.east": [(2, 0)],
            "idle.west": [(3, 0)],
            "walk.north": [(1, 0), (1, 1), (1, 0), (1, 2)],
            "walk.south": [(0, 0), (0, 1), (0, 0), (0, 2)],
            "walk.east": [(2, 0), (2, 1), (2, 0), (2, 2)],
            "walk.west": [(3, 0), (3, 1), (3, 0), (3, 2)],
            "sprint.north": [(1, 0), (1, 1), (1, 0), (1, 2)],
            "sprint.south": [(0, 0), (0, 1), (0, 0), (0, 2)],
            "sprint.east": [(2, 0), (2, 1), (2, 0), (2, 2)],
            "sprint.west": [(3, 0), (3, 1), (3, 0), (3, 2)],
        },
        "book": {
            "south": [(0, 0)],
            "north": [(1, 0)],
            "east": [(2, 0)],
            "west": [(3, 0)],
        }
    }
    
    SPEEDS = {
        "balan": {        
            "idle.north": 1,
            "idle.south": 1,
            "idle.east": 1,
            "idle.west": 1,
            "walk.north": 0.15,
            "walk.south": 0.15,
            "walk.east": 0.15,
            "walk.west": 0.15,
            "sprint.north": 0.25,
            "sprint.south": 0.25,
            "sprint.east": 0.25,
            "sprint.west": 0.25,
        },
        "book": {
            "north": 1,
            "south": 1,
            "east": 1,
            "west": 1,
        }
    }
    
    @classmethod
    def load(cls):
        log.info("- spritesheets")
        for sprite_name, frames in cls.FRAMES.items():
            surface = Resource[f"img.{sprite_name}"]
            
            surfaces = {}
            
            for animation_name, pos_list in frames.items():
                l = []
                for pos in pos_list:
                    x, y = pos
                    s = Surface((TILE_SIZE, TILE_SIZE), SRCALPHA)
                    s.blit(
                        surface,
                        (0, 0),
                        (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    )
                    l.append(s)
                    
                surfaces[animation_name] = l
                    
            Resource.add_animation(sprite_name, surfaces)
    
    def __init__(self, name: str):
        # self.frames = Resource[f"anim.{name}"]
        # self.speeds = self.SPEEDS[name]
        self.tmp = Resource.img(name)
        self.animation_name = name
        
    def change_animation(self, animation_name: str):
        # self.animation_name = animation_name
        # self.current_animation = self.frames[animation_name]
        # self.current_speed = self.speeds[animation_name]
        # self.current_frame_idx = 0
        pass
        
    def update(self, dt: int): # TODO : take care of 'dt'
        # self.current_frame_idx += self.current_speed
        # self.current_frame_idx %= len(self.current_animation)
        pass

    def get_surface(self) -> Surface:
        # return self.current_animation[int(self.current_frame_idx)]
        return self.tmp
