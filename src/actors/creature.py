from pygame.math import Vector2

from src.actors.entity import Entity
from src.commanding.command_node import CommandNode


class Creature(Entity):
    """
    Represents an entity with HP value
    """
    
    def __init__(self, pos: Vector2, hp_value: int):
        super().__init__(pos)

        self.brain = CommandNode()
        self.max_hp = hp_value
        self.hp = hp_value

    def dommage(self, points: int) -> None:
        self.hp -= points
        if self.hp < 0:
            self.hp = 0
    
    def heal(self, points: int) -> None:
        self.hp += points
        if self.hp > self.max_hp:
            self.hp = self.max_hp
