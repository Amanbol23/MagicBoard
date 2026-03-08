import customtkinter as ctk


class Task(ctk.CTkFrame):
    PRIORITY_COLORS = {
        "low": ("#4CAF50", "#66BB6A"),
        "medium": ("#FFA500", "#FFB833"),
        "high": ("#FF4444", "#FF6666")
    }

    def __init__(self, master, text, priority="low", on_delete=None):
        super().__init__(master, corner_radius=10, fg_color=("#3D3D3D", "#2D2D30"))
        self.text = text
        self.priority = priority
        self.on_delete = on_delete

        self.grid_columnconfigure(2, weight=1)

        self.priority_indicator = ctk.CTkFrame(
            master=self,
            width=4,
            height=30,
            corner_radius=2,
            fg_color=self.PRIORITY_COLORS.get(priority, self.PRIORITY_COLORS["low"])
        )
        self.priority_indicator.grid(row=0, column=0, padx=(8, 0), pady=10, sticky="w")

        self.checkbox = ctk.CTkCheckBox(
            master=self,
            text="",
            width=24,
            command=self._on_check
        )
        self.checkbox.grid(row=0, column=1, padx=(8, 5), pady=10, sticky="w")

        self.label = ctk.CTkLabel(
            master=self,
            text=text,
            font=ctk.CTkFont(size=14),
            anchor="w"
        )
        self.label.grid(row=0, column=2, padx=5, pady=10, sticky="w")

        self.delete_btn = ctk.CTkButton(
            master=self,
            text="✕",
            width=30,
            height=30,
            fg_color="transparent",
            hover_color=("#4A4A4D", "#3A3A3D"),
            command=self._delete_task
        )
        self.delete_btn.grid(row=0, column=3, padx=(5, 10), pady=10)

    def _on_check(self):
        if self.checkbox.get():
            self.label.configure(font=ctk.CTkFont(size=14, overstrike=True))
            self.priority_indicator.configure(fg_color=("gray60", "gray40"))
        else:
            self.label.configure(font=ctk.CTkFont(size=14, overstrike=False))
            self.priority_indicator.configure(
                fg_color=self.PRIORITY_COLORS.get(self.priority, self.PRIORITY_COLORS["low"])
            )

    def _delete_task(self):
        if self.on_delete:
            self.on_delete(self)
        self.destroy()

