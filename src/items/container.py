from src.items.item import Item


class Container:
    
    items: list[Item, None]
    
    def __init__(self, _len: int):
        self.items = [None for _ in range(_len)]
    
    def put(self, item: Item):
        for idx, _item in enumerate(self.items):
            if _item is None:
                self.items[idx] = item
                return
