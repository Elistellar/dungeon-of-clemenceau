from pygame.sprite import Group


class DataStorage(Group):

    obstacles = Group()
    update = Group()
        
    @classmethod
    def updateActors(cls, dt):
        cls.update.update(dt)
