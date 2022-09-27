from webbrowser import open_new_tab

from src.display.hud.menu.menu import Menu
from src.display.hud.menu.components.button import Button


class EscapeMenu(Menu):
    
    def about(self):
        open_new_tab("https://github.com/Elistellar/dungeon-of-clemenceau")
    
    # submenues = {
    #     "settings": ,
    # }
    
    components = {
        Button("menu.resume",   (540, 250, 200, 50), Menu.close),
        # Button("menu.settings", (540, 310, 200, 50), Menu.open_settings),
        Button("menu.about",    (540, 370, 200, 50), about),
        Button("menu.quit",     (540, 430, 200, 50), Menu.quit),
    }
