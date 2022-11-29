from src.display.hud.notification import Notification


class Achievement:
    
    _list = []
    
    def __init__(self, name: str, description: str):
        self.list.append(self)
        self.name = name
        self.description = description
        
        self.completed = False
        
    def complete(self):
        self.completed = True
        Notification.show("achievement", self.name)            
