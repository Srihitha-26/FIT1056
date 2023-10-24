# Third party imports
import tkinter as tk

from modules import Modules
from feedbackform import FeedbackForm
from progresstracker import ProgressTracker
from todo import Todo_List
from projectideas import ProjectIdeas


class StudentFrame(tk.Frame):
    """
    The class definition for the PatientFrame class.
    """

    def __init__(self, master, login_frame, user_obj):
        """
        The constructor for the PatientFrame class.
        """
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame
        self.user_obj = user_obj

        for row_count in range(5):
            self.master.rowconfigure(row_count, weight=1, uniform="row")

        self.master.columnconfigure(0, weight=1, uniform="col")

        # Display a dynamic welcome message using the patient's username
        welcome_label = tk.Label(self, text=f"Welcome back, {user_obj.get_first_name()}!")
        welcome_label.grid(row=0, column=0, padx=10, pady=10)

        # The modules button
        calculate_bmi_button = tk.Button(self, text="Modules", command=self.show_modules_frame)
        calculate_bmi_button.grid(row=1, column=0, padx=10, pady=10)

        # The progress tracker button
        view_profile_button = tk.Button(self, text="Progress Tracker", command=self.show_progress_frame)
        view_profile_button.grid(row=2, column=0, padx=10, pady=10)


        # The feedback form button
        view_appointments_button = tk.Button(self, text="Feedback Form", command=self.show_feedback_frame)
        view_appointments_button.grid(row=3, column=0, padx=10, pady=10)


        # The project ideas button
        view_appointments_button = tk.Button(self, text="Project Ideas", command=self.show_project_frame)
        view_appointments_button.grid(row=4, column=0, padx=10, pady=10)

        # The todo list button
        view_appointments_button = tk.Button(self, text="Todo-list", command=self.show_todo_frame)
        view_appointments_button.grid(row=5, column=0, padx=10, pady=10)

        # The logout button
        logout_button = tk.Button(self, text="Log out", command=self.logout)
        logout_button.grid(row=6, column=0, padx=10, pady=10)

    def show_modules_frame(self):
        """
        Event handler to show the modules frame.
        """
        self.place_forget()
        modules_frame = Modules(self.master, self)
        modules_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_feedback_frame(self):
        """
        Event handler to show the feedback form frame.
        """
        self.place_forget()
        feedback_frame = FeedbackForm(self.master, self)
        feedback_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_progress_frame(self):
        """
        Event handle to show the progress of the student frame
        """
        self.place_forget()
        progress_frame = ProgressTracker(self.master, self)
        progress_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_todo_frame(self):
        """
        Event handle to shows the todo-list for students
        """
        self.place_forget()
        todo_frame = Todo_List(self.master, self)
        todo_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_project_frame(self):
        """
        Event handle to shows personla project ideas for students
        """
        self.place_forget()
        project_frame = ProjectIdeas(self.master, self)
        project_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



    def logout(self):
        """
        Event handler to log out and return to the login screen.
        """
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

from week11_user import User

class Patient(User):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_first_name(self):
        return self.first_name


if __name__ == "__main__":
    pass
