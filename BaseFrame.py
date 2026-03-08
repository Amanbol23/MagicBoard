import customtkinter as ctk
import CustomButton as cb

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
        self.current_frame = None
        self.content_frames = {}

        self._setup_layout()
        self._setup_user_card()
        self._set_default_active_button()
        self.setup_content()

    def _setup_layout(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

    def _set_default_active_button(self):
        if self.nav_buttons:
            self.nav_buttons[0].set_active()

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
        for i in range(4):
            self.user_card.grid_rowconfigure(i, weight=0)
        self.user_card.grid_rowconfigure(4, weight=1)
        self.user_card.grid_rowconfigure(5, weight=0)

        menu_btn = cb.CustomButton(master=self.user_card, image=self.icons.menu_icon, frame_name="menu")
        menu_btn.grid(row=0, column=0, pady=(20, 8), padx=8)

        pomodoro_btn = cb.CustomButton(master=self.user_card, image=self.icons.pomodoro_icon, frame_name="pomodoro")
        pomodoro_btn.grid(row=1, column=0, pady=8, padx=8)

        stats_btn = cb.CustomButton(master=self.user_card, image=self.icons.stats_icon, frame_name="stats")
        stats_btn.grid(row=2, column=0, pady=8, padx=8)

        settings_btn = cb.CustomButton(master=self.user_card, image=self.icons.settings_icon, frame_name="settings")
        settings_btn.grid(row=5, column=0, pady=(8, 20), padx=8, sticky="s")

    def switch_active_frame(self, frame_name):
        if self.current_frame:
            self.current_frame.grid_forget()

        if frame_name in self.content_frames:
            self.current_frame = self.content_frames[frame_name]
            self.current_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    def register_frame(self, frame_name, frame_widget):
        self.content_frames[frame_name] = frame_widget

    @abstractmethod
    def setup_content(self):
        pass

