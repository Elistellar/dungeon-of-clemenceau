from src.display.hud.menu.components.button import Button
from src.display.hud.menu.components.key_input import KeyInput
from src.display.hud.menu.menu import Menu
from src.settings import Settings


class KeybindsMenu(Menu):
    """
    The 'Keybinds' settings menu
    """
    
    @classmethod
    def init(cls):
        
        wb = 80
        w = 180
        hb = 40
        h = 60
        
        keys = ( # max 20 with the above consts
            "move_forward",
            "move_backward",
            "move_left",
            "move_right",
            "sprint"
        )
        
        def gen_setter(name):
            def setter(val: int):
                Settings.set(f"key.{name}", val)
            return setter
        
        def gen_getter(name):
            def getter() -> int:
                return Settings[f"key.{name}"]
            return getter
        
        cls.components = tuple(
            
            KeyInput(
                "keybind." + name,
                (2 * wb + (i // 5) * (wb + w), 2 * hb + (i % 5) * (hb + h), w, h),
                gen_setter(name),
                gen_getter(name)
            ) for i, name in enumerate(keys)
            
        ) + (
            Button("menu.back", (540, 600, 200, 50), cls.close),
        )
