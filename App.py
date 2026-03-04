import datetime
import customtkinter as ctk

class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("840x720")
        self.title("")
        self.resizable(width=0, height=0)
        self.main_frame()
        self.mainloop()

    def main_frame(self):
        self.grid_rowconfigure(0, weight=1)

        user_card = ctk.CTkFrame(master=self, corner_radius=15, border_width=2)
        user_card.grid(row=0, column=0, sticky="nsew")

        # Размещаем элементы ВНУТРИ фрейма (master=user_card)
        label = ctk.CTkLabel(master=user_card, text="Профиль пользователя", font=("Arial", 20))
        label.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

        btn = ctk.CTkButton(master=user_card, text="Редактировать")
        btn.grid(row=1, column=0, sticky="nsew", pady=40, padx=10)
