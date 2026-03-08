from customtkinter import CTkImage
from PIL import Image

class Icon:
    def __init__(self):
        base_path = "icons/"
        icon_size = (24, 24)

        self.menu_icon = CTkImage(
            light_image=Image.open(f"{base_path}menu_icon.png"),
            dark_image=Image.open(f"{base_path}menu_icon.png"),
            size=icon_size
        )

        self.pomodoro_icon = CTkImage(
            light_image=Image.open(f"{base_path}pomodoro_icon.png"),
            dark_image=Image.open(f"{base_path}pomodoro_icon.png"),
            size=icon_size
        )

        self.add_icon = CTkImage(
            light_image=Image.open(f"{base_path}add_circle.png"),
            dark_image=Image.open(f"{base_path}add_circle.png"),
            size=icon_size
        )

        self.stats_icon = CTkImage(
            light_image=Image.open(f"{base_path}stats_icon.png"),
            dark_image=Image.open(f"{base_path}stats_icon.png"),
            size=icon_size
        )

        self.settings_icon = CTkImage(
            light_image=Image.open(f"{base_path}settings_icon.png"),
            dark_image=Image.open(f"{base_path}settings_icon.png"),
            size=icon_size
        )

