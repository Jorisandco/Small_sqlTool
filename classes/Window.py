from tkinter import Tk, Frame, Label, Button, StringVar, Entry, messagebox
from tkinter import ttk

class Window:
    def __init__(self, title: str, width: int, height: int):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)

        self.frame = Frame(self.root)
        self.frame.pack(padx=10, pady=10)

    def run(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()