from tkinter import Tk, messagebox


def show_game_crash_window(content: str):
    """
    Show a popup entilted 'Game crashed !'
    
    Parameters:
        content (str): The message on the popup
    """
    Tk().withdraw()
    messagebox.showerror("Game crashed !", "Game crashed unexpectedly :\n" + content)
