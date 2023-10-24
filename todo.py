import tkinter as tk

class Todo_List(tk.Frame):
    def __init__(self, master, student_frame):
        super().__init__(master)
        self.master = master
        self.student_frame = student_frame

        # Instructions for the user
        instruction_label = tk.Label(self, text="Please add all your tasks here")
        instruction_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.task_list = tk.Listbox(self, selectmode=tk.SINGLE)
        self.task_list.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.task_entry = tk.Entry(self)
        self.task_entry.grid(row=2, column=0, padx=10, pady=20)

        add_button = tk.Button(self, text="Add Task", command=self.add_task)
        remove_button = tk.Button(self, text="Remove Task", command=self.remove_task)

        add_button.grid(row=3, column=0, pady=5)
        remove_button.grid(row=3, column=1)

        # Bind the Enter key to the Add Task function for convenience.
        self.task_entry.bind("<Return>", lambda event=None: self.add_task())

        # Button to return to the student's main menu
        return_button = tk.Button(self, text="Return to Main Menu", command=self.return_to_menu)
        return_button.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.task_list.delete(selected_task)

    def return_to_menu(self):
        self.master.deiconify()
        self.destroy()
        self.student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    pass
