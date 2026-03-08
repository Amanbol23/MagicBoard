import customtkinter as ctk
from MainWindow import MainWindow


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("480x680")
        self.resizable(False, False)
        self.minsize(700, 600)
        self.title("Dash Board")
        ctk.set_default_color_theme("dark-blue")
        self.main = MainWindow(master=self)
        self.main.pack(fill="both", expand=True)
        self.mainloop()

