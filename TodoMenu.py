import customtkinter as ctk

from BaseContent import BaseContent
from Task import Task


class TodoMenu(BaseContent):
    MIN_WIDTH = 500
    MAX_WIDTH = 600
    MIN_HEIGHT = 500
    MAX_HEIGHT = 800

    def __init__(self, master):
        self.todo_frame = None
        self.add_button = None
        self.tasks = []

        super().__init__(master)

    def setup_widgets(self):
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.todo_frame = ctk.CTkScrollableFrame(
            master=self,
            corner_radius=12,
            label_text="To-Do List",
            label_font=ctk.CTkFont(family="Segoe UI", size=32, weight="bold"),
            width=self.MIN_WIDTH,
            height=self.MIN_HEIGHT,
            fg_color=("#2D2D30", "#252526"),
            bg_color="transparent"
        )
        self.todo_frame.grid(row=1, column=0, sticky="nw", padx=10, pady=(0, 10))

        self.input_frame = ctk.CTkFrame(
            master=self.todo_frame,
            fg_color="transparent"
        )
        self.input_frame.pack(fill="x", padx=10, pady=(10, 5))

        self.task_entry = ctk.CTkEntry(
            master=self.input_frame,
            placeholder_text="Enter new task...",
            height=40,
            corner_radius=10,
            width=200
        )
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.task_entry.bind("<Return>", lambda e: self._add_task())

        self.priority_var = ctk.StringVar(value="low")
        self.priority_menu = ctk.CTkOptionMenu(
            master=self.input_frame,
            values=["low", "medium", "high"],
            variable=self.priority_var,
            height=40,
            width=100,
            corner_radius=10
        )
        self.priority_menu.pack(side="left", padx=(0, 10))

        self.add_button = ctk.CTkButton(
            master=self.input_frame,
            text="+ Add",
            width=80,
            height=40,
            fg_color=("#007ACC", "#0A84FF"),
            hover_color=("#005A9E", "#0066CC"),
            corner_radius=10,
            command=self._add_task
        )
        self.add_button.pack(side="right")

        self._add_test_tasks()

    def _add_test_tasks(self):
        test_tasks = [
            ("Finish project documentation", "low"),
            ("Review pull requests", "medium"),
            ("defaultuser100001 - submit assignment", "high")
        ]
        for task_text, priority in test_tasks:
            self._create_task(task_text, priority)

    def _add_task(self):
        task_text = self.task_entry.get().strip()
        priority = self.priority_var.get()
        if task_text:
            self._create_task(task_text, priority)
            self.task_entry.delete(0, "end")
            self.priority_var.set("low")

    def _create_task(self, text, priority="low"):
        task = Task(
            master=self.todo_frame,
            text=text,
            priority=priority,
            on_delete=self._on_task_delete
        )
        task.pack(fill="x", padx=10, pady=5)
        self.tasks.append(task)

    def _on_task_delete(self, task):
        if task in self.tasks:
            self.tasks.remove(task)




