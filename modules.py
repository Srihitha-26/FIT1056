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

        for row_count in range(8):
            self.master.rowconfigure(row_count, weight=1, uniform="row")

        self.master.columnconfigure(0, weight=1, uniform="col")

        # Instructions for the user
        instruction_label = tk.Label(self, text="Please choose your module: ", font=("Arial", 10))
        instruction_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Create buttons for module options
        module_buttons = []
        for i, module_name in enumerate(self.modules.keys()):
            module_button = tk.Button(self, text=module_name, command=lambda name=module_name: self.open_module(name))
            module_button.grid(row=i + 1, column=0, padx=10, pady=10, columnspan=2)
            module_buttons.append(module_button)

        # Labeled Progress bar to track module completion
        self.progress_label = ttk.Label(self, text="Progress:")
        self.progress_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        # Progress bar to track module completion
        # self.progress = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        # self.progress.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.progress = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.progress.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

        # Label to display completion percentage
        self.percentage_label = tk.Label(self, text="0% complete")
        self.percentage_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Button to return to the student's main menu
        return_button = tk.Button(self, text="Return to Main Menu", command=self.return_to_menu)
        return_button.grid(row=8, column=0, padx=10, pady=10, columnspan=2)

        self.module_buttons = module_buttons

        # Dictionary to store MCQs and answers
        self.mcqs = {
            "Variables": {
                "What is a variable in Python?": {
                    "options": ["A. A constant value", "B. A reserved keyword", "C. A container for storing data", "D. A function in Python"],
                    "correct_answer": "C. A container for storing data"
                }
            },
            "Loops": {
                "What is a loop in Python?": {
                    "options": ["A. A Python keyword", "B. A container for storing data", "C. A control structure for repeating a block of code", "D. A function in Python"],
                    "correct_answer": "C. A control structure for repeating a block of code"
                }
            },
            "Strings": {
                "What is a string in Python?": {
                    "options": ["A. A constant value", "B. A reserved keyword", "C. A data type for text", "D. A function in Python"],
                    "correct_answer": "C. A data type for text"
                }
            },
            "Functions": {
                "What is a function in Python?": {
                    "options": ["A. A constant value", "B. A reserved keyword", "C. A block of reusable code", "D. A loop in Python"],
                    "correct_answer": "C. A block of reusable code"
                }
            }
        }

    def open_module(self, module_name):
        if not self.modules[module_name]:
            try:
                with open(f"{module_name}.txt", "r") as module_file:
                    module_text = module_file.read()

                module_frame = tk.Toplevel(self.master)
                module_frame.title(module_name)
                module_frame.geometry("680x500")

                module_frame.grid_rowconfigure(0, weight=1)
                module_frame.grid_columnconfigure(0, weight=1)
                
                text_label = tk.Label(module_frame, text=module_text)
                text_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

                mcq_button = tk.Button(module_frame, text="Show MCQ", command=lambda name=module_name: self.display_mcq(module_frame, name))
                mcq_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

            except FileNotFoundError:
                print(f"Text content for {module_name} not found.")
        else:
            messagebox.showinfo("Module Completion", f"You have already completed the '{module_name}' module.")

    def display_mcq(self, module_frame, module_name):
        if module_name in self.mcqs:
            mcq_frame = tk.Frame(module_frame)
            mcq_frame.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
            
            for question, mcq_data in self.mcqs[module_name].items():
                question_label = tk.Label(mcq_frame, text=question)
                question_label.pack()

                var = tk.StringVar()
                for option in mcq_data["options"]:
                    option_radio = tk.Radiobutton(mcq_frame, text=option, variable=var, value=option)
                    option_radio.pack()

                answer_button = tk.Button(mcq_frame, text="Submit Answer", command=lambda question=question, mcq_data=mcq_data, var=var: self.check_mcq_answer(question, mcq_data, var, mcq_frame))
                answer_button.pack()

        else:
            messagebox.showinfo("MCQ Not Found", f"No MCQ available for the '{module_name}' module.")

    def check_mcq_answer(self, question, mcq_data, answer_var, mcq_frame):
        correct_answer = mcq_data["correct_answer"]
        student_answer = answer_var.get()

        if student_answer == correct_answer:
            messagebox.showinfo("Correct Answer", "Your answer is correct and you've successfully completed this module!")
            self.modules[mcq_frame.master.title()] = True  # Mark the module as completed
            self.update_progress()  # Update the progress
            mcq_frame.destroy()
        else:
            retry_button = tk.Button(mcq_frame, text="Try Again", command=lambda: self.retry_mcq(mcq_frame, question, mcq_data))
            retry_button.pack()
            show_answer_button = tk.Button(mcq_frame, text="Show Answer", command=lambda: self.show_answer(question, mcq_data))
            show_answer_button.pack()


    def retry_mcq(self, mcq_frame, question, mcq_data):
        for widget in mcq_frame.winfo_children():
            widget.destroy()
        self.display_mcq(mcq_frame.master, mcq_frame.master.title())

    def show_answer(self, question, mcq_data):
        correct_answer = mcq_data["correct_answer"]
        messagebox.showinfo("Correct Answer", f"The correct answer is: {correct_answer}")

    # def complete_module(self, module_name, module_frame):
    #     response = messagebox.askquestion("Module Completion", f"Have you completed the '{module_name}' module?")
    #     if response == "yes":
    #         self.modules[module_name] = True
    #         # Update the progress bar and label
    #         self.update_progress()
        # module_frame.destroy()  # Close the module frame

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
