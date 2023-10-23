import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FeedbackForm(tk.Frame):
    def __init__(self, master, student_frame):
        super().__init__(master)
        self.master = master
        self.student_frame = student_frame

        # Create a label for the introductory text
        intro_label = ttk.Label(self, text="Please provide some feedback about CodeVenture so that it can be improved in the future.")
        intro_label.pack(pady=10)
        
        # Create a label for feedback
        feedback_label = ttk.Label(self, text="Question 1: Please provide your name")
        feedback_label.pack(pady=10)

        # Create a text entry field for the main feedback
        self.feedback_entry = ttk.Entry(self, width=50)
        self.feedback_entry.pack(pady=10)

        # Create labels and entry fields for additional questions
        question1_label = ttk.Label(self, text="Question 2: What did you like?")
        question1_label.pack()
        self.question1_entry = ttk.Entry(self, width=50)
        self.question1_entry.pack(pady=10)

        question2_label = ttk.Label(self, text="Question 3: What can be improved?")
        question2_label.pack()
        self.question2_entry = ttk.Entry(self, width=50)
        self.question2_entry.pack(pady=10)

        # Create a submit button
        submit_button = ttk.Button(self, text="Submit Feedback", command=self.submit_feedback)
        submit_button.pack(pady=10)

        # Button to return to the student's main menu
        return_button = tk.Button(self, text="Return to Main Menu", command=self.return_to_menu)
        return_button.pack(pady=10)

    def submit_feedback(self):
        feedback_text = self.feedback_entry.get()
        response1 = self.question1_entry.get()
        response2 = self.question2_entry.get()

        # Save the feedback and responses to a file
        with open("feedback.txt", "a") as feedback_file:
            feedback_file.write("Main Feedback: " + feedback_text + "\n")
            feedback_file.write("Response 1: " + response1 + "\n")
            feedback_file.write("Response 2: " + response2 + "\n")

        # Display a message to confirm feedback submission
        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")

        # Clear the entry fields
        self.feedback_entry.delete(0, 'end')
        self.question1_entry.delete(0, 'end')
        self.question2_entry.delete(0, 'end')

    def return_to_menu(self):
        """
        Event handler to return to the patient's main menu.
        """
        self.master.deiconify()  # Show the main window
        self.destroy()  # Destroy the module frame
        self.student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Show the patient frame

if __name__ == "__main__":
    pass
