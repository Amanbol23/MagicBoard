import customtkinter as ctk

from BaseContent import BaseContent


class PomodoroMenu(BaseContent):
    def __init__(self, master):
        super().__init__(master)

    def setup_widgets(self):
        # Настройка grid для центрирования
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Placeholder for Pomodoro content
        placeholder_label = ctk.CTkLabel(
            master=self,
            text="Pomodoro Timer Coming Soon!",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        placeholder_label.grid(row=0, column=0)
