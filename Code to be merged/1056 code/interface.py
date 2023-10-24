# Third party imports
import tkinter as tk

# Local application imports
from loginframe import LoginFrame


class Interface(tk.Tk):
    """
    Class definition for the Interface class
    """
    def __init__(self, title, width=1000, height=560):
        """
        Constructor for the Interface class,
        the main window for CodeVenture.
        :param title: str
        :param width: int - default 960 pixels
        :param height: int - default 540 pixels
        """
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")


if __name__ == "__main__":
    cv = Interface("CodeVenture")
    login = LoginFrame(cv)
    login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    cv.mainloop()
    print("--- End of program execution ---")
