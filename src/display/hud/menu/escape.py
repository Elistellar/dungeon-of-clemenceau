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
        Button("menu.resume",   (10, 10,  200, 50), Menu.close),
        # Button("menu.settings", (10, 70,  200, 50), Menu.open_settings),
        Button("menu.about",    (10, 130, 200, 50), about),
        Button("menu.quit",     (10, 190, 200, 50), Menu.quit),
    }
