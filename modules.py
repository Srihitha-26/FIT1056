import tkinter as tk
from tkinter import ttk, messagebox

class Modules(tk.Frame):
    def __init__(self, master, student_frame):
        super().__init__(master)
        self.master = master
        self.student_frame = student_frame

        # Define the module names and their completion status
        self.modules = {
            "Variables": False,
            "Loops": False,
            "Strings": False,
            "Functions": False
        }

        for row_count in range(7):
            self.master.rowconfigure(row_count, weight=1, uniform="row")

        self.master.columnconfigure(0, weight=1, uniform="col")

        # Instructions for the user
        instruction_label = tk.Label(self, text="Please choose your module")
        instruction_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Create buttons for module options
        module_buttons = []
        for i, module_name in enumerate(self.modules.keys()):
            module_button = tk.Button(self, text=module_name, command=lambda name=module_name: self.open_module(name))
            module_button.grid(row=i + 1, column=0, padx=10, pady=10, columnspan=2)
            module_buttons.append(module_button)

        # Progress bar to track module completion
        self.progress = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.progress.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Label to display completion percentage
        self.percentage_label = tk.Label(self, text="0% complete")
        self.percentage_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Button to return to the student's main menu
        return_button = tk.Button(self, text="Return to Main Menu", command=self.return_to_menu)
        return_button.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

        self.module_buttons = module_buttons

    def open_module(self, module_name):
        if not self.modules[module_name]:
            try:
                with open(f"{module_name}.txt", "r") as module_file:
                    module_text = module_file.read()

                module_frame = tk.Toplevel(self.master)
                module_frame.title(module_name)
                module_frame.geometry("400x300")
                text_label = tk.Label(module_frame, text=module_text)
                text_label.pack()

                # Configure a closing event for the module window
                completion_protocol = lambda name=module_name: self.on_closing(module_name, module_frame)
                module_frame.protocol("WM_DELETE_WINDOW", completion_protocol)

            except FileNotFoundError:
                print(f"Text content for {module_name} not found.")
        else:
            messagebox.showinfo("Module Completion", f"You have already completed the '{module_name}' module.")

    def on_closing(self, module_name, module_frame):
        response = messagebox.askquestion("Module Completion", f"Have you completed the '{module_name}' module?")
        if response == "yes":
            self.modules[module_name] = True
            # Update the progress bar and label
            self.update_progress()
        module_frame.destroy()  # Close the module frame

    def update_progress(self):
        completed_modules = sum(1 for status in self.modules.values() if status)
        total_modules = len(self.modules)
        progress_value = (completed_modules / total_modules) * 100
        self.progress["value"] = progress_value
        self.percentage_label["text"] = f"{int(progress_value)}% complete"
        
        if progress_value == 100:
            messagebox.showinfo("Congratulations", "You've completed all the given modules!")

    def return_to_menu(self):
        self.master.deiconify()
        self.destroy()
        self.student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    pass
