from src.actors.player import Player


def get_item(player: Player, item: type) -> bool:
    for _item in player.inventory.items:
        if type(_item) == item:
            return True
    
    return False
