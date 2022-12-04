from typing import Callable

from src.actors.player import Player
from src.display.hud.notification import Notification


class Achievement:
    
    _list = []
    
    def __init__(self, name: str, trigger: Callable[[Player], bool]):
        self._list.append(self)
        self.name = name
        self.__trigger = trigger
        
        self.completed = False
        
    def complete(self):
        self.completed = True
        Notification.show("achievement", self.name)
        
    def trigger(self, player: Player):
        if not self.completed and self.__trigger(player):
            self.complete()
    
    @classmethod
    def update(cls, player: Player):
        for achievement in cls._list:
            achievement.trigger(player)
