from src.display.hud.menu.components.button import Button
from src.display.hud.menu.components.slider import Slider
from src.display.hud.menu.menu import Menu
from src.settings import Settings
from src.sound import Sound


class AudioMenu(Menu):
    """
    The 'Audio' settings menu
    """
    
    @classmethod
    def init(cls):
        
        cls.components = (
            Slider(
                "menu.audio.entity", (490, 130, 300, 50), 0, 100,
                lambda v: Sound.set_channel_volume("entity", Settings.set("volume.entity", v)), Settings["volume.entity"]),
            Slider(
                "menu.audio.menu", (490, 245, 300, 50), 0, 100,
                lambda v: Sound.set_channel_volume("menu", Settings.set("volume.menu", v)), Settings["volume.menu"]),
            Slider(
                "menu.audio.music", (490, 360, 300, 50), 0, 100,
                lambda v: Sound.set_channel_volume("music", Settings.set("volume.music", v)), Settings["volume.music"]),            
            
            Button("menu.back", (540, 490, 200, 50), cls.close),
        )
