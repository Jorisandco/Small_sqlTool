from tkinter import Tk, Frame, Label, Button, StringVar, Entry, messagebox
from classes.SqlMethod import SqlMethod
from tkinter import ttk

class Window:
    def __init__(self, title: str, width: int, height: int):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.Sql = SqlMethod()
        self.frame = Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        if self.Sql.detect_mysql():
            self.state = "Close"
        else:
            self.state = "Start"
        
        self.Add_buttons([
            {'text': self.state, 'command': self.BootOrClose},
            {'text': 'close app', 'command': self.close}
        ])

    def run(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()

    def Add_buttons(self, buttons: list):
        for button in buttons:
            btn = Button(self.frame, text=button['text'], command=button['command'])
            btn.pack(pady=5)

    def remove_buttons(self):
        for widget in self.frame.winfo_children():
            if isinstance(widget, Button):
                widget.destroy()
        
    def BootOrClose(self):
        if self.state == "Start":
            self.Sql.boot_mysql()
        else:
            self.Sql.close_mysql()


        self.state = "Close" if self.state == "Start" else "Start"
        self.remove_buttons()
        self.Add_buttons([
            {'text': self.state, 'command': self.BootOrClose},
            {'text': 'close app', 'command': self.close}
        ])