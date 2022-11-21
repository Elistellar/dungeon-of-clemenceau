from pygame.sprite import Group
from src.actors.entity import Entity

class DataStorage(Group):

    entities = Group()
    obstacles = Group()
    
    def updateActors(cls, dt):
        cls.all_actors.update(dt)

