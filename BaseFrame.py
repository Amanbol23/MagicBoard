import customtkinter as ctk
import CustomeButton as cb

from abc import ABC, abstractmethod
from Icons import Icon


class BaseFrame(ctk.CTkFrame, ABC):
    def __init__(self, master):
        super().__init__(master)
        self.icons = Icon()
        self.user_card = None
        self.content_area = None
        self.nav_buttons = []
        self.active_button = None

        self._setup_layout()
        self._setup_user_card()
        self.setup_content()

    def _setup_layout(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

    def _setup_user_card(self):
        self.user_card = ctk.CTkFrame(
            master=self,
            corner_radius=0,
            border_width=0,
            width=56,
            fg_color=("#E0E0E0", "#1A1A1A")
        )

        self.user_card.grid(row=0, column=0, sticky="ns", padx=0, pady=0)
        self.user_card.grid_propagate(False)

        self.user_card.grid_columnconfigure(0, weight=1)
        for i in range(3):
            self.user_card.grid_rowconfigure(i, weight=0)
        self.user_card.grid_rowconfigure(3, weight=1)


        menu_btn = cb.CustomButton(master=self.user_card, image=self.icons.menu_icon)
        menu_btn.grid(row=0, column=0, pady=(20, 8), padx=8)

        pomodoro_btn = cb.CustomButton(master=self.user_card, image=self.icons.pomodoro_icon)
        pomodoro_btn.grid(row=1, column=0, pady=8, padx=8)

    @abstractmethod
    def setup_content(self):
        pass

