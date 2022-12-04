from src.display.hud.menu.base import BaseMenu
from src.display.hud.menu.components.large_button import LargeButton
from src.display.hud.menu.components.key_input import KeyInput


class KeybindsMenu(BaseMenu):
    
    @classmethod
    def init(cls):
        cls.components = (
            (KeyInput((436, 190), "keybind.move_forward", "move_forward"),   KeyInput((576, 190), "keybind.move_left", "move_left"),   None),
            (KeyInput((436, 290), "keybind.move_backward", "move_backward"), KeyInput((576, 290), "keybind.move_right", "move_right"), None),
            (KeyInput((436, 390), "keybind.sprint", "sprint"),               None,                                                     None),
            (None,                                                           LargeButton((512, 466), "menu.back", cls.back),           None),
        )

        # X X KeyInput((716, 190))
        # X X KeyInput((716, 290))
        # X KeyInput((576, 390)) KeyInput((716, 390))
