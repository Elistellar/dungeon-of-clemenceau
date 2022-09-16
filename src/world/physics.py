from src.world.obstacles import Obstacles


class Physics:
    
    @staticmethod
    def collide_x(entity):
        for sprite in Obstacles.sprites():
            if entity.hitbox.colliderect(sprite.rect):
                if entity.direction.x > 0:
                    entity.pos.x -= entity.hitbox.right - sprite.rect.left
                    entity.hitbox.right = sprite.rect.left
                else:
                    entity.pos.x += sprite.rect.right - entity.hitbox.left
                    entity.hitbox.left = sprite.rect.right

    @staticmethod
    def collide_y(entity):
        for sprite in Obstacles.sprites():
            if entity.hitbox.colliderect(sprite.rect):
                
                if entity.direction.y > 0:
                    entity.pos.y -= entity.hitbox.bottom - sprite.rect.top
                    entity.hitbox.bottom = sprite.rect.top
                else:
                    entity.pos.y += sprite.rect.bottom - entity.hitbox.top
                    entity.hitbox.top = sprite.rect.bottom