import customtkinter as ctk

from BaseContent import BaseContent


class PomodoroMenu(BaseContent):
    WORK_TIME = 25 * 60
    SHORT_BREAK = 5 * 60
    LONG_BREAK = 15 * 60

    def __init__(self, master):
        self.time_left = self.WORK_TIME
        self.is_running = False
        self.is_work_session = True
        self.sessions_completed = 0
        self.timer_job = None

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

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.content_frame = ctk.CTkFrame(
            master=self.main_frame,
            fg_color="transparent"
        )
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.title_label = ctk.CTkLabel(
            master=self.content_frame,
            text="Pomodoro Timer",
            font=ctk.CTkFont(family="Segoe UI", size=28, weight="bold")
        )
        self.title_label.pack(pady=(30, 10))

        self.status_label = ctk.CTkLabel(
            master=self.content_frame,
            text="WORK SESSION",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("#FF6B6B", "#FF6B6B")
        )
        self.status_label.pack(pady=(10, 20))

        self.timer_frame = ctk.CTkFrame(
            master=self.content_frame,
            corner_radius=100,
            width=200,
            height=200,
            fg_color=("#3D3D3D", "#1E1E1E")
        )
        self.timer_frame.pack(pady=20)
        self.timer_frame.pack_propagate(False)

        self.timer_label = ctk.CTkLabel(
            master=self.timer_frame,
            text=self._format_time(self.time_left),
            font=ctk.CTkFont(family="Consolas", size=48, weight="bold")
        )
        self.timer_label.place(relx=0.5, rely=0.5, anchor="center")

        self.sessions_label = ctk.CTkLabel(
            master=self.content_frame,
            text="Sessions: 0/4",
            font=ctk.CTkFont(size=14)
        )
        self.sessions_label.pack(pady=(10, 20))

        self.buttons_frame = ctk.CTkFrame(
            master=self.content_frame,
            fg_color="transparent"
        )
        self.buttons_frame.pack(pady=10)

        self.start_btn = ctk.CTkButton(
            master=self.buttons_frame,
            text="Start",
            width=100,
            height=40,
            corner_radius=10,
            fg_color=("#4CAF50", "#45a049"),
            hover_color=("#45a049", "#3d8b40"),
            command=self._toggle_timer
        )
        self.start_btn.grid(row=0, column=0, padx=5)

        self.reset_btn = ctk.CTkButton(
            master=self.buttons_frame,
            text="Reset",
            width=100,
            height=40,
            corner_radius=10,
            fg_color=("#FF6B6B", "#e55555"),
            hover_color=("#e55555", "#cc4444"),
            command=self._reset_timer
        )
        self.reset_btn.grid(row=0, column=1, padx=5)

        self.skip_btn = ctk.CTkButton(
            master=self.buttons_frame,
            text="Skip",
            width=100,
            height=40,
            corner_radius=10,
            fg_color=("#6B7280", "#555555"),
            hover_color=("#555555", "#444444"),
            command=self._skip_session
        )
        self.skip_btn.grid(row=0, column=2, padx=5)

        self.info_frame = ctk.CTkFrame(
            master=self.content_frame,
            fg_color="transparent"
        )
        self.info_frame.pack(pady=(20, 10))

        info_text = "Work: 25min | Short Break: 5min | Long Break: 15min"
        self.info_label = ctk.CTkLabel(
            master=self.info_frame,
            text=info_text,
            font=ctk.CTkFont(size=11),
            text_color=("gray50", "gray60")
        )
        self.info_label.pack()

    def _format_time(self, seconds):
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02d}:{secs:02d}"

    def _toggle_timer(self):
        if self.is_running:
            self._pause_timer()
        else:
            self._start_timer()

    def _start_timer(self):
        self.is_running = True
        self.start_btn.configure(text="Pause", fg_color=("#FFA500", "#e59400"))
        self._tick()

    def _pause_timer(self):
        self.is_running = False
        self.start_btn.configure(text="Start", fg_color=("#4CAF50", "#45a049"))
        if self.timer_job:
            self.after_cancel(self.timer_job)
            self.timer_job = None

    def _tick(self):
        if self.is_running and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text=self._format_time(self.time_left))
            self.timer_job = self.after(1000, self._tick)
        elif self.time_left == 0:
            self._session_complete()

    def _session_complete(self):
        self.is_running = False
        self.start_btn.configure(text="Start", fg_color=("#4CAF50", "#45a049"))

        if self.is_work_session:
            self.sessions_completed += 1
            self.sessions_label.configure(text=f"Sessions: {self.sessions_completed}/4")

            if self.sessions_completed % 4 == 0:
                self.time_left = self.LONG_BREAK
                self.status_label.configure(
                    text="LONG BREAK",
                    text_color=("#4ECDC4", "#4ECDC4")
                )
            else:
                self.time_left = self.SHORT_BREAK
                self.status_label.configure(
                    text="SHORT BREAK",
                    text_color=("#4ECDC4", "#4ECDC4")
                )
            self.is_work_session = False
        else:
            self.time_left = self.WORK_TIME
            self.status_label.configure(
                text="WORK SESSION",
                text_color=("#FF6B6B", "#FF6B6B")
            )
            self.is_work_session = True

        self.timer_label.configure(text=self._format_time(self.time_left))

    def _reset_timer(self):
        self._pause_timer()
        self.time_left = self.WORK_TIME
        self.is_work_session = True
        self.timer_label.configure(text=self._format_time(self.time_left))
        self.status_label.configure(
            text="WORK SESSION",
            text_color=("#FF6B6B", "#FF6B6B")
        )

    def _skip_session(self):
        self._pause_timer()
        self._session_complete()
