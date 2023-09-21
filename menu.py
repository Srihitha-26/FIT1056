"""
FIT1056 Software Development Phase
Student name: Yong Wen Jian
Student ID: 33561583
Group: MA_FRI_1600_G2
"""


from users import *

class Menu:
    def __init__(self):
        self.user = None

    def set_user(self, newUser: User) -> bool: 
        if newUser == None or isinstance(newUser, User):
            self.user = newUser
            return True
        else:
            return False
        
    def get_user(self) -> User:
        return self.user
    
    def main_menu(self):
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
    
    def create_account_type_menu(self,typeList: list[str]):
        print("Choose account type:\n")
        return typeList


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

