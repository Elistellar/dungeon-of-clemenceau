from src.display.hud.menu.audio import AudioMenu
from src.display.hud.menu.escape import EscapeMenu
from src.display.hud.menu.keybinds import KeybindsMenu
from src.display.hud.menu.lang import LangMenu
from src.display.hud.menu.settings import SettingsMenu


def load_menus():
    EscapeMenu.init()
    SettingsMenu.init()
    KeybindsMenu.init()
    AudioMenu.init()
    LangMenu.init()
