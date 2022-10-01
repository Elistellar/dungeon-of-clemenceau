from pygame.mouse import get_pos, get_pressed, get_visible, set_visible


class Mouse:
    
    @classmethod
    def disable(cls):
        set_visible(False)
    
    @classmethod
    def activate(cls):
        set_visible(True)
    
    @classmethod
    def get_pos(cls) -> tuple[int, int]:
        if get_visible():
            return get_pos()
        else:
            return (-1, -1)
        
    @classmethod
    def get_pressed(cls, btn: int) -> bool:
        """
        btn :
         - 0 -> left
         - 1 -> middle
         - 2 -> right
        """
        return get_pressed()[btn]
