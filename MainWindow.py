import customtkinter as ctk

from BaseFrame import BaseFrame
from TodoMenu import TodoMenu
from PomodoroMenu import PomodoroMenu
from StatsMenu import StatsMenu
from SettingsMenu import SettingsMenu


class MainWindow(BaseFrame):
    def __init__(self, master):
        super().__init__(master)

    def setup_content(self):
        self.content_area = ctk.CTkFrame(master=self, corner_radius=0)
        self.content_area.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)

        self.content_area.grid_rowconfigure(0, weight=1)
        self.content_area.grid_columnconfigure(0, weight=1)

        todo_menu = TodoMenu(master=self.content_area)
        self.register_frame("menu", todo_menu)

        pomodoro_menu = PomodoroMenu(master=self.content_area)
        self.register_frame("pomodoro", pomodoro_menu)

        stats_menu = StatsMenu(
            master=self.content_area,
            todo_menu=todo_menu,
            pomodoro_menu=pomodoro_menu
        )
        self.register_frame("stats", stats_menu)

        settings_menu = SettingsMenu(master=self.content_area)
        self.register_frame("settings", settings_menu)

        self.switch_active_frame("menu")
