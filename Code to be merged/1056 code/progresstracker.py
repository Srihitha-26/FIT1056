import tkinter as tk
from tkinter import ttk

class ProgressTracker(tk.Frame):
    def _init_(self, master, student_frame):
        super()._init_(master)
        self.master = master
        self.student_frame = student_frame

        # Create a progress bar
        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=20)

        # Create a label to display progress percentage
        self.progress_label = ttk.Label(self.master, text="Progress: 0%")
        self.progress_label.pack()

        # Create buttons to increase and decrease progress
        increase_button = ttk.Button(self.master, text="Increase Progress", command=self.increase_progress)
        increase_button.pack(pady=10)

        decrease_button = ttk.Button(self.master, text="Decrease Progress", command=self.decrease_progress)
        decrease_button.pack(pady=10)

        # Button to return to the student's main menu
        return_button = tk.Button(self, text="Return to Main Menu", command=self.return_to_menu)
        return_button.grid(row=5, column=0, padx=10, pady=10)

    def increase_progress(self):
        current_value = self.progress_bar["value"]
        if current_value < 100:
            new_value = current_value + 10
            self.progress_bar["value"] = new_value
            self.update_progress_label(new_value)

    def decrease_progress(self):
        current_value = self.progress_bar["value"]
        if current_value > 0:
            new_value = current_value - 10
            self.progress_bar["value"] = new_value
            self.update_progress_label(new_value)

    def update_progress_label(self, value):
        self.progress_label["text"] = f"Progress: {value}%"

    def return_to_menu(self):
        self.master.deiconify()
        self.destroy()
        self.student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



if __name__ == "__main__":
    pass