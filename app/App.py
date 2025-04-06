from app.settings import config

from tkinter import Tk, font
from app.Frame import TextFrame, NavigationFrame

class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('900x600')
        self.title('Notebook')

        text_field_font = font.Font(
            self,
            family=config.text_font,
            size=config.text_font_size,
        )

        text_navigation_font = font.Font(
            self,
            family=config.navigation_font,
            size=config.navigation_font_size,
        )

        self.text_frame = TextFrame(self, text_field_font)
        self.text_field = self.text_frame.text_field

        NavigationFrame(self, self.text_field, text_navigation_font).pack(fill='x')

        self.text_frame.pack(fill='both', expand=True)
