from pygame import Surface
from pygame.locals import SRCALPHA

from src.utils.consts import TILE_SIZE


class SpriteSheet:
    
    def __init__(self, surface: Surface, frames: dict[str, list[tuple[int, int]]], speeds: dict[str, float]):
        
        self.frames = {}
        
        for name, pos_list in frames.items():
            
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
            
            self.frames[name] = l
            
        self.speeds = speeds
        
    def change_animation(self, animation_name: str):
        self.animation_name = animation_name
        self.current_animation = self.frames[animation_name]
        self.current_speed = self.speeds[animation_name]
        self.current_frame_idx = 0
        
    def update(self, dt: int):            
        self.current_frame_idx += self.current_speed
        self.current_frame_idx %= len(self.current_animation)
        # print(self.current_frame_idx)

    def get_surface(self) -> Surface:
        return self.current_animation[int(self.current_frame_idx)]
