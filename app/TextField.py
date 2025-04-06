import os
from app.settings import config

from tkinter import Text, messagebox, simpledialog, filedialog
from sys import argv

class TextField(Text):
    def __init__(self, master, font):
        super().__init__(master)
        self.configure(
            font=font,
            background=config.bg_color,
            foreground=config.fg_color,
            insertbackground=config.fg_color
        )

        try:
            self.filename = self._check_file_extension(argv[1])
        except IndexError:
            self.filename = None
        else:
            try:
                with open(self.filename, "r", encoding='utf-8') as file:
                    self.file_text = file.read()
            except FileNotFoundError:
                with open(self.filename, "w", encoding='utf-8') as file:
                    file.write("")
                    self.file_text = ""
            finally:
                self.insert('end', self.file_text)

    def save_file(self):
        if self.filename is not None:
            try:
                with open(self.filename, "w", encoding='utf-8') as file:
                    file.write(self.get(1.0, 'end'))
            except TypeError:
                messagebox.showerror('Error', 'Filename cannot be empty')
        else:
            new_filename = simpledialog.askstring("File", "Enter file name:")
            if new_filename is not None:
                self.filename = self._check_file_extension(new_filename)
                self.save_file()
            else:
                return

    def new_file(self):
        try:
            new_filename = simpledialog.askstring("File", "Enter file name:")
            if self._check_filename(new_filename) is None:
                return
        except FileExistsError:
            messagebox.showerror("Error", "File name already exists")
            self.new_file()
        else:
            self.delete(1.0, 'end')
            self.filename = new_filename
            with open(self.filename, "w", encoding='utf-8') as file:
                file.write("")

    def open_file(self):
        temp_directory_path = filedialog.askopenfilename()
        if temp_directory_path != '':
            self.filename = temp_directory_path

            with open(self.filename, "r", encoding='utf-8') as file:
                self.file_text = file.read()
            self.delete(1.0, 'end')
            self.insert('end', self.file_text)
        else:
            return

    @staticmethod
    def _check_file_extension(file_name):
        try:
            file = file_name.split(".", 1)[::-1]
        except AttributeError:
            return None

        if len(file) > 1 and len(file[0]) > 0:
            return file_name
        else:
            return file_name + config.file_extension

    @staticmethod
    def _check_filename(filename):
        if TextField._check_file_extension(filename) in os.listdir(os.getcwd()):
            raise FileExistsError
