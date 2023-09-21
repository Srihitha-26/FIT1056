from menu import Menu
from users import *
from game import *

class Login:
    menu = Menu()
    game = Game()

    def auth_account(self,usernameInput: str, passwordInput: str, accounts: list[str]):
        result = False
        for i in range(len(accounts)):
            if accounts[i][0] == usernameInput:
                if accounts[i][1] == passwordInput:
                    self.accountIndex = i
                    result = True
                break
        return result

    def create_account(accountType: str, allIDs: list[str], **kwargs) -> User:
        # TODO: Add accounts into files here.
        newUser = User("Placeholder","Placeholder","Placeholder@email.nul")
        while True:
            usernameInput = input("\nPlease enter a username: ")
            if newUser.set_username(usernameInput):
                break
        while True:
            passwordInput = input("\nPlease enter your password: ")
            if newUser.set_password(passwordInput):
                break
        while True:
            emailInput = input("\nPlease enter your email: ")
            if newUser.set_email(emailInput):
                break
        newUser.generate_id(allIDs)
        
        match accountType:
            case "Investor":
                newUser = Investor(newUser.get_username, newUser.get_password, newUser.get_email, 0)
                while True:
                    sharesInput = input("\nPlease enter the current amount of shares that is held (%): ")
                    if newUser.set_shares(sharesInput):
                        break

            case "Educator":
                newUser = Educator(newUser.get_username, newUser.get_password, newUser.get_email, "exschool")
                while True:
                    schoolInput = input("\nPlease enter the name of the school that you are teaching at: ")
                    if newUser.set_school(schoolInput):
                        break

            case "Student":
                newUser = Student(newUser.get_username, newUser.get_password, newUser.get_email)

                while True:
                    educationInput = input("\nAre you a student of an educator for this program? (Y/N): ").upper()
                    if educationInput == "Y":
                        while True:
                            educatorInput = input("\nPlease enter the username of your educator: ")
                            found = False
                            for i in range(kwargs['edus'][0]):
                                if educatorInput == kwargs['edus'][0][i]:
                                    studentEducator = Educator(kwargs['edus'][0][i], kwargs['edus'][1][i], kwargs['edus'][2][i], kwargs['edus'][3][i])
                                    newUser.set_educator(studentEducator)
                                    found = True
                                    break
                            if found:
                                break
                            else:
                                print("Educator not found.")

                        
                        while True:
                            schoolInput = input("\nPlease enter the name of the school that you are learning at: ")
                            if newUser.set_school(schoolInput):
                                break
                        break

                    elif educationInput == "N":
                        break

                    else:
                        print("Invalid Input.")

            case _:
                print("No account type matched")
                return None
                        
        return newUser

        
    def login(self):
        devFile = open("./database/devs.txt", "r", encoding="utf8")
        lines = list(devFile)
        devUsernames = []
        devPasswords = []
        devAccounts = []
        devEmails = []
        devTypes = []
        devIDs = []
        devStartTimes = []
        devEndTimes = []

        for line in lines:
            (username, password, email, type, devID, startTime, endTime) = line.strip("\n").split(",")
            devUsernames.append(username)
            devPasswords.append(password)
            devAccounts.append([username,password])
            devEmails.append(email)
            devTypes.append(type)
            devIDs.append(devID)
            devStartTimes.append(startTime)
            devEndTimes.append(endTime)

        invFile = open("./database/invs.txt", "r", encoding="utf8")
        lines = list(invFile)
        invUsernames = []
        invPasswords = []
        invAccounts = []
        invEmails = []
        invTypes = []
        invIDs = []
        invShares = []

        for line in lines:
            (username, password, email, type, invID, shares) = line.strip("\n").split(",")
            invUsernames.append(username)
            invPasswords.append(password)
            invAccounts.append([username,password])
            invEmails.append(email)
            invTypes.append(type)
            invIDs.append(invID)
            invShares.append(shares)

        eduFile = open("./database/edus.txt", "r", encoding="utf8")
        lines = list(eduFile)
        eduUsernames = []
        eduPasswords = []
        eduAccounts = []
        eduEmails = []
        eduTypes = []
        eduIDs = []
        eduSchools = []


        for line in lines:
            (username, password, email, type, eduID, school) = line.strip("\n").split(",")
            eduUsernames.append(username)
            eduPasswords.append(password)
            eduAccounts.append([username,password])
            eduEmails.append(email)
            eduTypes.append(type)
            eduIDs.append(eduID)
            eduSchools.append(school)

        stuFile = open("./database/stus.txt", "r", encoding="utf8")
        lines = list(stuFile)
        stuUsernames = []
        stuPasswords = []
        stuAccounts = []
        stuEmails = []
        stuTypes = []
        stuIDs = []
        stuSchools = []
        stuEducator = []


        for line in lines:
            (username, password, email, type, stuID, school, educator) = line.strip("\n").split(",")
            stuUsernames.append(username)
            stuPasswords.append(password)
            stuAccounts.append([username,password])
            stuEmails.append(email)
            stuTypes.append(type)
            stuIDs.append(stuID)
            stuSchools.append(school)
            stuEducator.append(educator)

        allIDs = [devIDs, invIDs, eduIDs, stuIDs]

        while True:
            selectedOption = self.menu.option_select(self.menu.main_menu())
            match selectedOption:
                case "Log In":
                    usernameInput = input("\nPlease enter your username: ")
                    passwordInput = input("\nPlease enter your password: ")
                    if self.auth_account(usernameInput,passwordInput,devAccounts):
                        self.menu.set_user(Developer(devUsernames[self.accountIndex], devPasswords[self.accountIndex], devEmails[self.accountIndex], [devStartTimes[self.accountIndex],devEndTimes[self.accountIndex]]))
                    elif self.auth_account(usernameInput,passwordInput,invAccounts):
                        self.menu.set_user(Investor(invUsernames[self.accountIndex], invPasswords[self.accountIndex], invEmails[self.accountIndex], invShares[self.accountIndex]))
                    elif self.auth_account(usernameInput,passwordInput,eduAccounts):
                        self.menu.set_user(Educator(eduUsernames[self.accountIndex], eduPasswords[self.accountIndex], eduEmails[self.accountIndex], eduSchools[self.accountIndex]))
                    elif self.auth_account(usernameInput,passwordInput,stuAccounts):
                        for i in range(len(eduUsernames)):
                            if stuEducator[self.accountIndex] == eduUsernames[i]:
                                studentEducator = Educator(eduUsernames[i], eduPasswords[i], eduEmails[i], eduSchools[i])
                                break
                        self.menu.set_user(Student(stuUsernames[self.accountIndex], stuPasswords[self.accountIndex], stuEmails[self.accountIndex], stuSchools[self.accountIndex], studentEducator))

                case "Create Account":
                    typeOption = self.menu.option_select(self.menu.create_account_type_menu(User.availableTypes))
                    newAccount = self.create_account(typeOption, allIDs, edus=[eduUsernames,eduPasswords,eduEmails,eduSchools])
                    self.menu.set_user(newAccount)

                case "Exit Program":
                    print("Exiting program...")
                    break

                case "View Shares":
                    print(f"Shares: {self.menu.get_user().get_shares()}%")

                case "Buy Shares":
                    print(f"Current Shares: {self.menu.get_user().get_shares()}%")
                    while True:
                        try:
                            sharesInput = float(input("\nPlease enter the percentage(%) of shares to buy: "))
                        except ValueError:
                            print("Invalid amount of shares.")
                        
                        if sharesInput > (100 - self.menu.get_user().get_shares()):
                            print("Owned shares cannot surpass 100%")
                        elif sharesInput < 0:
                            print("Cannot buy negative shares")
                        else:
                            self.menu.get_user().set_shares(sharesInput + self.menu.get_user().get_shares())
                            print(f"Bought {sharesInput}% of shares.")
                            break

                case "Sell Shares":
                    print(f"Current Shares: {self.menu.get_user().get_shares()}%")
                    while True:
                        try:
                            sharesInput = float(input("\nPlease enter the percentage(%) of shares to sell: "))
                        except ValueError:
                            print("Invalid amount of shares.")
                        
                        if sharesInput > self.menu.get_user().get_shares():
                            print("Sold shares cannot surpass owned shares.")
                        elif sharesInput < 0:
                            print("Cannot sell negative shares")
                        else:
                            self.menu.get_user().set_shares(self.menu.get_user().get_shares() - sharesInput)
                            print(f"Sold {sharesInput}% of shares.")
                            break


                case "Set New Working Times":
                    print(f"Current working times: {self.menu.get_user().get_times()[0]} - {self.menu.get_user().get_times()[1]}")
                    while True:
                        startInput = input("Set new starting time (HH:MM): ")
                        endInput = input("Set new ending time (HH:MM): ")
                        if self.menu.get_user().set_times([startInput, endInput]):
                            break

                case "Add Quizzes":
                    self.game.create_quiz()
                
                case "Remove Quizzes":
                    self.game.remove_quiz()
                
                case "Attempt Quizzes":
                    self.game.attemptQuizzes()
                
                case "Change Associated School":
                    while True:
                        schoolInput = input("Please enter the new school name: ")
                        if self.menu.get_user().set_school(schoolInput):
                            break

                case "Set Educator":
                    while True:
                        educatorInput = input("\nPlease enter the username of your educator: ")
                        found = False
                        for i in range(eduUsernames):
                            if educatorInput == eduUsernames:
                                studentEducator = Educator(eduUsernames[i], eduPasswords[i], eduEmails[i], eduSchools[i])
                                if self.menu.get_user().set_educator(studentEducator):
                                    found = True
                                    break
                        if found:
                            break
                        else:
                            print("Educator not found.")
                
                case "View Profile":
                    print(str(self.menu.get_user()))
                
                case "Change Password":
                    tries = 0
                    passed = False
                    while True:
                        oldPass = input("Please enter the current password: ")
                        if oldPass == self.menu.get_user().get_password():
                            passed = True
                            break
                        else:
                            tries += 1
                            print("Password is incorrect")
                            if tries > 2:
                                print("Tries exceeded, returning to menu.")
                                break
                    
                    while passed:
                        newPass = input("Please enter the new password: ")
                        if self.menu.get_user().set_password(newPass):
                            confirmPass = input("Please re-enter the new password: ")
                            if self.menu.get_user().get_password() == confirmPass:
                                print("New password set.")
                                break
                            else:
                                print("Re-entered password does not match the new password.")
                
                case "Log Out":
                    print("Logging out.")
                    self.menu.set_user(None)

                case "Delete Account":
                    while True:
                        confirmInput = input("Confirm account deletion? (Y/N): ").upper()
                        if confirmInput == "Y":
                            self.menu.set_user(None)
                            # TODO: Add deletion in files here.
                            break
                        elif confirmInput == "N":
                            print("Deletion cancelled, returning to menu.")
                            break
                        else:
                            print("Invalid input.")
                    