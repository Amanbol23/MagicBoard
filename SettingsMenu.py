import customtkinter as ctk

from BaseContent import BaseContent


class SettingsMenu(BaseContent):
    def __init__(self, master, app=None):
        self.app = app
        super().__init__(master)

    def setup_widgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(
            master=self,
            corner_radius=12,
            fg_color=("#2D2D30", "#252526")
        )
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.title_label = ctk.CTkLabel(
            master=self.main_frame,
            text="Settings",
            font=ctk.CTkFont(family="Segoe UI", size=28, weight="bold")
        )
        self.title_label.pack(pady=(30, 30))

        self.settings_frame = ctk.CTkFrame(
            master=self.main_frame,
            fg_color="transparent"
        )
        self.settings_frame.pack(fill="both", expand=True, padx=40, pady=10)

        self.theme_frame = ctk.CTkFrame(
            master=self.settings_frame,
            fg_color=("#3D3D3D", "#1E1E1E"),
            corner_radius=10
        )
        self.theme_frame.pack(fill="x", pady=10)

        self.theme_label = ctk.CTkLabel(
            master=self.theme_frame,
            text="Theme",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.theme_label.pack(side="left", padx=20, pady=15)

        self.theme_var = ctk.StringVar(value="Dark")
        self.theme_menu = ctk.CTkOptionMenu(
            master=self.theme_frame,
            values=["Dark", "System"],
            variable=self.theme_var,
            width=150,
            height=35,
            corner_radius=8,
            command=self._change_theme
        )
        self.theme_menu.pack(side="right", padx=20, pady=15)

        self.scale_frame = ctk.CTkFrame(
            master=self.settings_frame,
            fg_color=("#3D3D3D", "#1E1E1E"),
            corner_radius=10
        )
        self.scale_frame.pack(fill="x", pady=10)

        self.scale_label = ctk.CTkLabel(
            master=self.scale_frame,
            text="UI Scale",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.scale_label.pack(side="left", padx=20, pady=15)

        self.scale_var = ctk.StringVar(value="100%")
        self.scale_menu = ctk.CTkOptionMenu(
            master=self.scale_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            variable=self.scale_var,
            width=150,
            height=35,
            corner_radius=8,
            command=self._change_scale
        )
        self.scale_menu.pack(side="right", padx=20, pady=15)

        self.pomodoro_frame = ctk.CTkFrame(
            master=self.settings_frame,
            fg_color=("#3D3D3D", "#1E1E1E"),
            corner_radius=10
        )
        self.pomodoro_frame.pack(fill="x", pady=10)

        self.pomodoro_label = ctk.CTkLabel(
            master=self.pomodoro_frame,
            text="Pomodoro Duration",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.pomodoro_label.pack(side="left", padx=20, pady=15)

        self.pomodoro_var = ctk.StringVar(value="25 min")
        self.pomodoro_menu = ctk.CTkOptionMenu(
            master=self.pomodoro_frame,
            values=["15 min", "20 min", "25 min", "30 min", "45 min"],
            variable=self.pomodoro_var,
            width=150,
            height=35,
            corner_radius=8
        )
        self.pomodoro_menu.pack(side="right", padx=20, pady=15)

        self.notif_frame = ctk.CTkFrame(
            master=self.settings_frame,
            fg_color=("#3D3D3D", "#1E1E1E"),
            corner_radius=10
        )
        self.notif_frame.pack(fill="x", pady=10)

        self.notif_label = ctk.CTkLabel(
            master=self.notif_frame,
            text="Notifications",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.notif_label.pack(side="left", padx=20, pady=15)

        self.notif_switch = ctk.CTkSwitch(
            master=self.notif_frame,
            text="",
            width=50
        )
        self.notif_switch.pack(side="right", padx=20, pady=15)
        self.notif_switch.select()

        self.about_frame = ctk.CTkFrame(
            master=self.settings_frame,
            fg_color=("#3D3D3D", "#1E1E1E"),
            corner_radius=10
        )
        self.about_frame.pack(fill="x", pady=10)

        self.about_label = ctk.CTkLabel(
            master=self.about_frame,
            text="About",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.about_label.pack(side="left", padx=20, pady=15)

        self.version_label = ctk.CTkLabel(
            master=self.about_frame,
            text="MagicBoard v1.0 | defaultuser100001",
            font=ctk.CTkFont(size=14),
            text_color=("gray50", "gray60")
        )
        self.version_label.pack(side="right", padx=20, pady=15)

    def _change_theme(self, choice):
        theme_map = {
            "Light": "light",
            "Dark": "dark",
            "System": "system"
        }
        ctk.set_appearance_mode(theme_map.get(choice, "dark"))

    def _change_scale(self, choice):
        scale_map = {
            "80%": 0.8,
            "90%": 0.9,
            "100%": 1.0,
            "110%": 1.1,
            "120%": 1.2
        }
        ctk.set_widget_scaling(scale_map.get(choice, 1.0))

