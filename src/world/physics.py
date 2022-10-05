from typing import TYPE_CHECKING

from src.world.groups import Obstacles

if TYPE_CHECKING:
    from src.entities.entity import Entity


class Physics:
    """
    Handle all game physics.
    """
    
    @staticmethod
    def collide_x(entity: "Entity"):
        """
        Compute the horizontal collision between the given entity and the obstacle group.
        """
        for sprite in Obstacles.sprites():
            if entity.hitbox.colliderect(sprite.rect):
                if entity.direction.x > 0:
                    entity.pos.x -= entity.hitbox.right - sprite.rect.left
                    entity.hitbox.right = sprite.rect.left
                else:
                    entity.pos.x += sprite.rect.right - entity.hitbox.left
                    entity.hitbox.left = sprite.rect.right

    @staticmethod
    def collide_y(entity: "Entity"):
        """
        Compute the horizontal collision between the given entity and the obstacle group.
        """
        for sprite in Obstacles.sprites():
            if entity.hitbox.colliderect(sprite.rect):
                
                if entity.direction.y > 0:
                    entity.pos.y -= entity.hitbox.bottom - sprite.rect.top
                    entity.hitbox.bottom = sprite.rect.top
                else:
                    entity.pos.y += sprite.rect.bottom - entity.hitbox.top
                    entity.hitbox.top = sprite.rect.bottom
