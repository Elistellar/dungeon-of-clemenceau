from src.display.hud.menu.base import BaseMenu
from src.display.hud.menu.components.large_button import LargeButton
from src.display.hud.menu.components.slider import Slider
from src.sounds.sound import Sound


class SoundMenu(BaseMenu):
    
    @classmethod
    def init(cls):
        cls.components = (
            (Slider((512, 178), "menu.audio.music",  lambda: Sound.channels.get("music") * 100,  lambda v: Sound.set_channel_volume("music", v),  0, 100),),
            (Slider((512, 254), "menu.audio.entity", lambda: Sound.channels.get("entity") * 100, lambda v: Sound.set_channel_volume("entity", v), 0, 100),),
            (Slider((512, 330), "menu.audio.menu",   lambda: Sound.channels.get("menu") * 100,   lambda v: Sound.set_channel_volume("menu", v),   0, 100),),
            (LargeButton((512, 418), "menu.back", cls.back),),
        )
