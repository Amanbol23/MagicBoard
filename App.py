import customtkinter as ctk
from MainWindow import MainWindow

class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("840x720")
        self.title("Dash Board")
        self.main = MainWindow(master=self)
        self.main.pack(fill="both", expand=True)
        self.mainloop()

