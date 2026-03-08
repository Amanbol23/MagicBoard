import customtkinter as ctk
from abc import ABC, abstractmethod


class BaseContent(ctk.CTkFrame, ABC):

    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.setup_widgets()

    @abstractmethod
    def setup_widgets(self):
        pass

