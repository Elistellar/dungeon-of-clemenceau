from tkinter import Tk, messagebox


def show_game_crash_window(content: str):
    Tk().withdraw()
    messagebox.showerror("Game crashed !", "Game crashed unexpectedly :\n" + content)
