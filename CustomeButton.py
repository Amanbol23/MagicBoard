import customtkinter as ctk

class CustomButton(ctk.CTkButton):
    def __init__(self, master, image=None):
        super().__init__(master=master, image=image,
                         text="",
                         width=40, height=40,
                         fg_color="transparent", hover_color=("#E5E5E5", "#2B2B2B"),
                         compound="left",
                         border_width=0, corner_radius=10
                         )

        self.base_frame = self.master.master

        if hasattr(self.base_frame, "nav_buttons"):
            self.base_frame.nav_buttons.append(self)

        self.configure(command=self.set_active)

    def set_active(self):
        if self.base_frame.active_button:
            self.base_frame.active_button.configure(fg_color="transparent")

        self.base_frame.active_button = self
        self.configure(fg_color=("#CFCFCF", "#3D3D3D"))
