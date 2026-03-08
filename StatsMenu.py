import customtkinter as ctk

from BaseContent import BaseContent


class StatsMenu(BaseContent):
    def __init__(self, master, todo_menu=None, pomodoro_menu=None):
        self.todo_menu = todo_menu
        self.pomodoro_menu = pomodoro_menu

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

        self.charts_frame = ctk.CTkFrame(
            master=self.main_frame,
            fg_color="transparent"
        )
        self.charts_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.tasks_chart_frame = ctk.CTkFrame(
            master=self.charts_frame,
            fg_color=("#3D3D3D", "#1E1E1E"),
            corner_radius=12
        )
        self.tasks_chart_frame.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)

        self.tasks_title = ctk.CTkLabel(
            master=self.tasks_chart_frame,
            text="Tasks Today",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.tasks_title.pack(pady=(20, 15))

        self.tasks_canvas = ctk.CTkCanvas(
            master=self.tasks_chart_frame,
            width=200,
            height=200,
            bg="#1E1E1E",
            highlightthickness=0
        )
        self.tasks_canvas.pack(pady=15)

        self.tasks_legend_frame = ctk.CTkFrame(
            master=self.tasks_chart_frame,
            fg_color="transparent"
        )
        self.tasks_legend_frame.pack(pady=15)

        self.completed_label = ctk.CTkLabel(
            master=self.tasks_legend_frame,
            text="● Completed: 0",
            font=ctk.CTkFont(size=14),
            text_color=("#4CAF50", "#66BB6A")
        )
        self.completed_label.pack(anchor="w")

        self.pending_label = ctk.CTkLabel(
            master=self.tasks_legend_frame,
            text="● Pending: 0",
            font=ctk.CTkFont(size=14),
            text_color=("#FF6B6B", "#FF6B6B")
        )
        self.pending_label.pack(anchor="w")

        self.pomodoro_chart_frame = ctk.CTkFrame(
            master=self.charts_frame,
            fg_color=("#3D3D3D", "#1E1E1E"),
            corner_radius=12
        )
        self.pomodoro_chart_frame.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)

        self.pomodoro_title = ctk.CTkLabel(
            master=self.pomodoro_chart_frame,
            text="Pomodoro Time",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.pomodoro_title.pack(pady=(20, 15))

        self.pomodoro_canvas = ctk.CTkCanvas(
            master=self.pomodoro_chart_frame,
            width=200,
            height=200,
            bg="#1E1E1E",
            highlightthickness=0
        )
        self.pomodoro_canvas.pack(pady=15)

        self.pomodoro_legend_frame = ctk.CTkFrame(
            master=self.pomodoro_chart_frame,
            fg_color="transparent"
        )
        self.pomodoro_legend_frame.pack(pady=15)

        self.work_time_label = ctk.CTkLabel(
            master=self.pomodoro_legend_frame,
            text="● Work: 0 min",
            font=ctk.CTkFont(size=14),
            text_color=("#FF6B6B", "#FF6B6B")
        )
        self.work_time_label.pack(anchor="w")

        self.break_time_label = ctk.CTkLabel(
            master=self.pomodoro_legend_frame,
            text="● Break: 0 min",
            font=ctk.CTkFont(size=14),
            text_color=("#4ECDC4", "#4ECDC4")
        )
        self.break_time_label.pack(anchor="w")

        self.sessions_label = ctk.CTkLabel(
            master=self.pomodoro_legend_frame,
            text="Sessions: 0",
            font=ctk.CTkFont(size=14),
            text_color=("gray60", "gray60")
        )
        self.sessions_label.pack(anchor="w", pady=(5, 0))

        self.refresh_btn = ctk.CTkButton(
            master=self.main_frame,
            text="Refresh",
            width=150,
            height=40,
            corner_radius=10,
            fg_color=("#007ACC", "#0A84FF"),
            hover_color=("#005A9E", "#0066CC"),
            command=self.update_stats
        )
        self.refresh_btn.pack(pady=(0, 20))

        self.update_stats()

    def _draw_pie_chart(self, canvas, values, colors, size=180):
        canvas.delete("all")

        total = sum(values)
        center_x = size // 2 + 10
        center_y = size // 2 + 10

        if total == 0:
            canvas.create_text(
                center_x, center_y,
                text="No data",
                fill="gray60",
                font=("Segoe UI", 14)
            )
            return

        start_angle = 90
        radius = size // 2

        non_zero_count = sum(1 for v in values if v > 0)

        if non_zero_count == 1:
            for i, value in enumerate(values):
                if value > 0:
                    canvas.create_oval(
                        10, 10, size + 10, size + 10,
                        fill=colors[i],
                        outline="#1E1E1E",
                        width=2
                    )
                    break
        else:
            for i, value in enumerate(values):
                if value > 0:
                    extent = (value / total) * 360
                    canvas.create_arc(
                        10, 10, size + 10, size + 10,
                        start=start_angle,
                        extent=-extent,
                        fill=colors[i],
                        outline="#1E1E1E",
                        width=2
                    )
                    start_angle -= extent

        inner_radius = radius * 0.55
        canvas.create_oval(
            center_x - inner_radius,
            center_y - inner_radius,
            center_x + inner_radius,
            center_y + inner_radius,
            fill="#1E1E1E",
            outline="#1E1E1E"
        )

        percentage = (values[0] / total) * 100 if values[0] > 0 else 0
        canvas.create_text(
            center_x, center_y,
            text=f"{percentage:.0f}%",
            fill="white",
            font=("Segoe UI", 18, "bold")
        )

    def update_stats(self):
        completed_tasks = 0
        pending_tasks = 0

        if self.todo_menu and hasattr(self.todo_menu, 'tasks'):
            for task in self.todo_menu.tasks:
                if hasattr(task, 'checkbox') and task.checkbox.get():
                    completed_tasks += 1
                else:
                    pending_tasks += 1

        self._draw_pie_chart(
            self.tasks_canvas,
            [completed_tasks, pending_tasks],
            ["#4CAF50", "#FF6B6B"]
        )
        self.completed_label.configure(text=f"● Completed: {completed_tasks}")
        self.pending_label.configure(text=f"● Pending: {pending_tasks}")

        sessions = 0
        work_minutes = 0
        break_minutes = 0

        if self.pomodoro_menu:
            sessions = self.pomodoro_menu.sessions_completed
            work_minutes = sessions * 25
            break_minutes = sessions * 5

        self._draw_pie_chart(
            self.pomodoro_canvas,
            [work_minutes, break_minutes],
            ["#FF6B6B", "#4ECDC4"]
        )
        self.work_time_label.configure(text=f"● Work: {work_minutes} min")
        self.break_time_label.configure(text=f"● Break: {break_minutes} min")
        self.sessions_label.configure(text=f"Sessions: {sessions}")


