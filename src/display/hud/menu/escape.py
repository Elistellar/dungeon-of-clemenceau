from webbrowser import open_new_tab

from src.display.hud.menu.components.button import Button
from src.display.hud.menu.menu import Menu
from src.display.hud.menu.settings import SettingsMenu


class EscapeMenu(Menu):
    
    submenues = {
        "settings": SettingsMenu,
    }
    
    @classmethod
    def init(cls):
        cls.components = (
            Button("menu.quit",     (540, 250, 200, 50), cls.quit),
            Button("menu.settings", (540, 310, 200, 50), cls.open_sub, ("settings",)),
            Button("menu.about",    (540, 370, 200, 50), open_new_tab, ("https://github.com/Elistellar/dungeon-of-clemenceau",)),
            Button("menu.resume",   (540, 430, 200, 50), cls.close),
        )
