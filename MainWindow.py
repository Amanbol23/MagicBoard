import customtkinter as ctk

from BaseFrame import BaseFrame

class MainWindow(BaseFrame):
    def __init__(self, master):
        super().__init__(master)

    def setup_content(self):
        self.content_area = ctk.CTkFrame(master=self, corner_radius=0)
        self.content_area.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
