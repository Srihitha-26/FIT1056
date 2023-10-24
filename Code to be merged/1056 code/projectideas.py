import tkinter as tk

class ProjectIdeas(tk.Frame):
    """
    A simple Tkinter interface for displaying project ideas of varying complexity levels (easy, intermediate, and advanced).
    Users can click the "Return to Main Menu" button to go back to the main menu.
    """
    def __init__(self, master, student_frame):
        """
        Initialize the ProjectIdeas class.

        Args:
            master: The master (parent) widget.
            student_frame: The student frame to return to when clicking "Return to Main Menu."
        """
        super().__init__(master)
        self.master = master
        self.student_frame = student_frame

        # Button to return to the student's main menu
        return_button = tk.Button(self, text="Return to Main Menu", command=self.return_to_menu)
        return_button.grid(row=5, column=0, padx=10, pady=10)

        # Create labels with project ideas

        # Easy project ideas
        easy_ideas_text = """
        Easy Project Ideas:
        1. Create a To-Do List App: Build a simple to-do list application.
        2. Design a Personal Blog: Develop a blog with user-friendly features.
        3. Build a Calculator: Create a basic calculator app.
        """
        easy_ideas_label = tk.Label(self, text=easy_ideas_text, font=("Arial", 12))
        easy_ideas_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Intermediate project ideas
        intermediate_ideas_text = """
        Intermediate Project Ideas:
        4. Develop a Weather App: Show weather information for a chosen location.
        5. Build a Budget Tracker: Manage and track your expenses.
        6. Create a Recipe Finder: Find recipes based on available ingredients.
        """
        intermediate_ideas_label = tk.Label(self, text=intermediate_ideas_text, font=("Arial", 12))
        intermediate_ideas_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Advanced project ideas
        advanced_ideas_text = """
        Advanced Project Ideas:
        7. Create an E-Commerce Website: Build a fully functional online store.
        8. Develop a Social Media Platform: Create a social network with user profiles.
        9. Build a Machine Learning Model: Develop a machine learning project.
        """
        advanced_ideas_label = tk.Label(self, text=advanced_ideas_text, font=("Arial", 12))
        advanced_ideas_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    def return_to_menu(self):
        """
        Return to the student's main menu by deiconifying the master frame, destroying the current frame, and placing the student frame at the center.
        """
        self.master.deiconify()
        self.destroy()
        self.student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    pass
