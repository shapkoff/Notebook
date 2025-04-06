import tkinter as tk
from app.settings import config

from app.TextField import TextField

class NavigationFrame(tk.Frame):
    def __init__(self, master, text_field, font):
        super().__init__(master)

        self.configure(background=config.bg_color)

        tk.Button(
            self,
            text='New',
            command=text_field.new_file,
            font=font,
            background=config.bg_color,
            foreground=config.fg_color,
            activebackground=config.bg_color,
            activeforeground=config.fg_color,
        ).grid(row=0, column=0)

        tk.Button(
            self,
            text='Open',
            command=text_field.open_file,
            font=font,
            background=config.bg_color,
            foreground=config.fg_color,
            activebackground=config.bg_color,
            activeforeground=config.fg_color,
        ).grid(row=0, column=1)


        tk.Button(
            self,
            text='Save',
            command=text_field.save_file,
            font=font,
            background=config.bg_color,
            foreground=config.fg_color,
            activebackground=config.bg_color,
            activeforeground=config.fg_color,
        ).grid(row=0, column=2)


class TextFrame(tk.Frame):
    def __init__(self, master, font):
        super().__init__(master)

        self.text_field = TextField(self, font)

        self.text_field.pack(fill="both", expand=True)