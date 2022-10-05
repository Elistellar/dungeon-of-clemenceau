from pygame.mouse import get_pos, get_pressed, get_visible, set_visible


class Mouse:
    """
    Handle the mouse. 
    """
    
    @classmethod
    def disable(cls):
        """
        Hide the mouse
        """
        set_visible(False)
    
    @classmethod
    def activate(cls):
        """
        Show the mouse
        """
        set_visible(True)
    
    @classmethod
    def get_pos(cls) -> tuple[int, int]:
        """
        Returns the mouse position. If the mouse is disabled, returns (-1, -1).
        """
        if get_visible():
            return get_pos()
        else:
            return (-1, -1)
        
    @classmethod
    def get_pressed(cls, btn: int) -> bool:
        """        
        Parameters:
            btn (int): The mouse button to get, 0 for left, 1 for middle and 2 for right.
            
        Returns:
            A boolean if the button requested is pressed.
        """
        return get_pressed()[btn]
