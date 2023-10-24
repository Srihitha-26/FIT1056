# Third party imports
import tkinter as tk

# Local application imports
from week11_authenticator import Authenticator
from students_menu import StudentFrame
from week11_user import User


class LoginFrame(tk.Frame):
    """
    The class definition for the LoginFrame class.
    """

    def __init__(self, master):
        """
        Constructor for the LoginFrame class.
        :param master: Tk object; the main window that the
                       login frame is to be contained.
        """
        super().__init__(master=master)
        self.master = master

        login_canvas = tk.Canvas(master=self, width=200, height=200)
        login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

    
        image_path = "images/image.png"
        self.login_logo = tk.PhotoImage(file=image_path)
        login_canvas.create_image(0, 0,
                                  anchor=tk.NW,
                                  image=self.login_logo)

        login_title = tk.Label(master=self,
                               text="CodeVenture App",
                               font=("Arial Bold", 25))
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        login_tagline = tk.Label(master=self,
                               text="An amazing platform to learn Python",
                               font=("Calibre", 14))
        login_tagline.grid(row=2, columnspan=2, padx=10, pady=10)

        username_label = tk.Label(master=self, text="Username:")
        username_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)

        self.username = tk.StringVar()
        self.username_entry = tk.Entry(master=self, textvariable=self.username)
        self.username_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

        password_label = tk.Label(master=self, text="Password:")
        password_label.grid(row=4, column=0, sticky=tk.E, padx=10, pady=10)

        self.password = tk.StringVar()
        self.password_entry = tk.Entry(master=self, textvariable=self.password,
                                  show="●")
        self.password_entry.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)

        login_button = tk.Button(master=self, text="Login",
                                 command=self.authenticate_login)
        login_button.grid(row=6, columnspan=2, padx=10, pady=10)

        self.login_text = tk.StringVar()
        login_message = tk.Label(master=self, textvariable=self.login_text)

        login_message.grid(row=5, columnspan=2, padx=10, pady=10)

    def authenticate_login(self):
        """
        Frontend function for the authentication procedure.
        This is invoked when the login button is clicked.
        :return: None
        """
        authenticator = Authenticator()
        auth_res = authenticator.authenticate(self.username.get(),
                                              self.password.get())

        if isinstance(auth_res, User):
            self.password_entry.delete(0, 'end')
            self.username_entry.delete(0, "end")
                                                                    
            if auth_res.get_role() == "PA":  # patient login

                self.place_forget()

                # Create and display the Patient login frame
                patient_frame = StudentFrame(self.master, self, auth_res)
                patient_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            elif auth_res.get_role() in ["AD", "RE"]:
                self.login_text.set("Login successfully!")
        else:
            self.login_text.set("Failed to login")


if __name__ == "__main__":
    pass
