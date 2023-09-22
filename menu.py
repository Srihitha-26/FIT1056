"""
FIT1056 Software Development Phase
Student name: Yong Wen Jian
Student ID: 33561583
Group: MA_FRI_1600_G2
"""


from users import *
"""
The menu class represents what function options can be displayed to the user.
"""
class Menu:
    """
    Constructor for the Menu class
    """
    def __init__(self):
        self.user = None

    """
    Sets the user of the menu
    :param newUser: A user instance to be put into the menu
    :return: A boolean representing if the new user is set successfully
    """
    def set_user(self, newUser: User) -> bool: 
        if newUser == None or isinstance(newUser, User):
            self.user = newUser
            return True
        else:
            return False
    

    """
    Gets the current user of the menu class
    :return: The user instance using the menu class
    """
    def get_user(self) -> User:
        return self.user
    
    """
    The main menu representing the functions that the current user can interact with.
    :return: A list of strings representing the allowable actions of the user
    """
    def main_menu(self) -> list[str]:
        menuOptions = []
        if self.user == None:
            menuOptions.append("Log In")
            menuOptions.append("Create Account")
            menuOptions.append("Exit Program")
        else:
            if isinstance(self.user, Investor):
                menuOptions.append("View Shares")
                menuOptions.append("Buy Shares")
                menuOptions.append("Sell Shares")
            elif isinstance(self.user, Developer):
                menuOptions.append("Set New Working Times")
            elif isinstance(self.user, Educator):
                menuOptions.append("Add Quizzes")
                menuOptions.append("Remove Quizzes")
                menuOptions.append("Change Associated School")
            elif isinstance(self.user, Student):
                menuOptions.append("Attempt Quizzes")
                menuOptions.append("Change Associated School")
                menuOptions.append("Set Educator")

            menuOptions.append("View Profile")
            menuOptions.append("Change Password")
            menuOptions.append("Log Out")
            menuOptions.append("Delete Account")

        return menuOptions
    
    """
    The menu given when user chooses to create an account
    :return: A list of types of account that can be made in the system.
    """
    def create_account_type_menu(self,typeList: list[str]):
        print("Choose account type:\n")
        return typeList

    """
    Provides numbering for a list of options and prompting the user to choose the option
    :param optionList: A list of strings containing the allowable actions in the given menu
    :return: A string representing the user's chosen option
    """
    def option_select(self,optionList: list[str]) -> str:
        for i in range(len(optionList)):
            print(f"{i+1}) {optionList[i]}")

        while True:
            try:
                userInput = int(float(input("\nPlease select an option: ")))
                if userInput > len(optionList) or userInput < 1:
                    print("Please select a valid number.")
                else:
                    break
            except ValueError:
                print("Please select a valid number.")
        
        return optionList[(userInput - 1)]

