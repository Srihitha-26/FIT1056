"""
FIT1056 Software Development Phase
Student name: Yong Wen Jian
Student ID: 33561583
Group: MA_FRI_1600_G2
"""


from menu import Menu
from users import *
from game import *
import os

class Login:
    menu = Menu()
    game = Game()
    baseFile = os.path.dirname(os.path.realpath('__file__'))
    
    devsData = os.path.join(baseFile,'database\devs.txt')
    invsData = os.path.join(baseFile,'database\invs.txt')
    edusData = os.path.join(baseFile,'database\edus.txt')
    stusData = os.path.join(baseFile,'database\stus.txt')

    def auth_account(self,usernameInput: str, passwordInput: str, accounts: list[str]):
        result = False
        for i in range(len(accounts)):
            if accounts[i][0] == usernameInput:
                if accounts[i][1] == passwordInput:
                    self.accountIndex = i
                    result = True
                break
        return result

    def create_account(self,accountType: str, allIDs: list[str], allUsernames: list[str], **kwargs) -> User:
        newUser = User("Placeholder","Placeholder","Placeholder@email.nul")
        while True:
            usernameInput = input("\nPlease enter a username: ")
            if newUser.set_username(usernameInput):
                if newUser.get_username() not in allUsernames:
                    break
                else:
                    print("Username has been taken.")
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
                        with open(self.invsData, "a") as file:
                            file.write(f"{newUser.get_username()},{newUser.get_password()},{newUser.get_email()},{newUser.get_id()},{newUser.get_shares()}")
                            file.close()
                        break

            case "Educator":
                newUser = Educator(newUser.get_username, newUser.get_password, newUser.get_email, "exschool")
                while True:
                    schoolInput = input("\nPlease enter the name of the school that you are teaching at: ")
                    if newUser.set_school(schoolInput):
                        with open(self.edusData, "a") as file:
                            file.write(f"{newUser.get_username()},{newUser.get_password()},{newUser.get_email()},{newUser.get_id()},{newUser.get_school()}")
                            file.close()
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
                                print("Educator username not found in database.")

                        
                        while True:
                            schoolInput = input("\nPlease enter the name of the school that you are learning at: ")
                            if newUser.set_school(schoolInput):
                                with open(self.stusData, "a") as file:
                                    file.write(f"{newUser.get_username()},{newUser.get_password()},{newUser.get_email()},{newUser.get_id()},{newUser.get_school()},{newUser.get_educator().get_username()}")
                                    file.close()
                                break
                        break

                    elif educationInput == "N":
                        with open(self.stusData, "a") as file:
                            file.write(f"{newUser.get_username()},{newUser.get_password()},{newUser.get_email()},{newUser.get_id()},None,None")
                            file.close()
                        break

                    else:
                        print("Invalid Input.")

            case _:
                print("No account type matched")
                return None
                        
        return newUser
    

    def delete_account(self,user: User):
        userType = user.get_type()

        match userType:
            case "DEV":
                userFile = self.devsData
            case "INV":
                userFile = self.invsData
            case "EDU":
                userFile = self.edusData
            case "STU":
                userFile = self.stusData

        # Read the existing user data from the file
        with open(userFile, "r") as file:
            lines = file.readlines()
            file.close()

        # Create a new list of lines without the user's data
        new_lines = []
        user_found = False
        for line in lines:
            allData = line.strip().split(",")
            existing_username = allData[0]
            if existing_username != user.get_username():
                new_lines.append(line)
            else:
                user_found = True
                       
        # If the user was found and their data removed, update the file
        if user_found:
            with open(userFile, "w") as file:
                file.writelines(new_lines)
                file.close()
            return True  # Account successfully deleted
        else:
            return False  # User not found


    def login_main(self):
        devFile = open(self.devsData, "r", encoding="utf8")
        lines = list(devFile)
        devFile.close()
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

        invFile = open(self.invsData, "r", encoding="utf8")
        lines = list(invFile)
        invFile.close()
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

        eduFile = open(self.edusData, "r", encoding="utf8")
        lines = list(eduFile)
        eduFile.close()
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

        stuFile = open(self.stusData, "r", encoding="utf8")
        lines = list(stuFile)
        stuFile.close()
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

        allUsernames = [devUsernames, invUsernames, eduUsernames, stuUsernames]
        allIDs = [devIDs, invIDs, eduIDs, stuIDs]

        while True:
            selectedOption = self.menu.option_select(self.menu.main_menu())
            match selectedOption:
                case "Log In":
                    usernameInput = input("\nPlease enter your username: ")
                    passwordInput = input("\nPlease enter your password: ")
                    if self.auth_account(usernameInput,passwordInput,devAccounts):
                        self.menu.set_user(Developer(devUsernames[self.accountIndex], devPasswords[self.accountIndex], devEmails[self.accountIndex], [devStartTimes[self.accountIndex],devEndTimes[self.accountIndex]], userID=devIDs[self.accountIndex]))
                    elif self.auth_account(usernameInput,passwordInput,invAccounts):
                        self.menu.set_user(Investor(invUsernames[self.accountIndex], invPasswords[self.accountIndex], invEmails[self.accountIndex], invShares[self.accountIndex], userID=invIDs[self.accountIndex]))
                    elif self.auth_account(usernameInput,passwordInput,eduAccounts):
                        self.menu.set_user(Educator(eduUsernames[self.accountIndex], eduPasswords[self.accountIndex], eduEmails[self.accountIndex], eduSchools[self.accountIndex], userID=eduIDs[self.accountIndex]))
                    elif self.auth_account(usernameInput,passwordInput,stuAccounts):
                        if stuSchools[self.accountIndex] == 'None':
                            studentSchool = None
                        else:
                            studentSchool = stuSchools[self.accountIndex]
                        studentEducator = None
                        for i in range(len(eduUsernames)):
                            if stuEducator[self.accountIndex] == eduUsernames[i]:
                                studentEducator = Educator(eduUsernames[i], eduPasswords[i], eduEmails[i], eduSchools[i], userID=eduIDs[i])
                                break     
                        self.menu.set_user(Student(stuUsernames[self.accountIndex], stuPasswords[self.accountIndex], stuEmails[self.accountIndex], studentSchool, studentEducator, userID=stuIDs[self.accountIndex]))
                    else:
                        print("Invalid account username or password, returning to menu.")

                case "Create Account":
                    typeOption = self.menu.option_select(self.menu.create_account_type_menu(User.availableTypes))
                    self.menu.set_user(self.create_account(typeOption, allIDs, allUsernames, edus=[eduUsernames,eduPasswords,eduEmails,eduSchools]))
                    

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
                    print("Saving data.")
                    userType = self.menu.get_user().get_type()

                    match userType:
                        case "DEV":
                            userFile = self.devsData
                        case "INV":
                            userFile = self.invsData
                        case "EDU":
                            userFile = self.edusData
                        case "STU":
                            userFile = self.stusData

                    # Read the existing user data from the file
                    with open(userFile, "r") as file:
                        lines = file.readlines()
                        file.close()

                    # Create a new list of lines with the updated user's data
                    new_lines = []
                    for line in lines:
                        allData = line.strip().split(",")
                        existing_username = allData[0]
                        if existing_username != self.menu.get_user().get_username():
                            new_lines.append(line)
                        else:
                            new_lines.append(self.menu.get_user().to_database())
                    
                    with open(userFile, "w") as file:
                        file.writelines(new_lines)
                        file.close()

                    print("Logging out.")
                    self.menu.set_user(None)

                case "Delete Account":
                    while True:
                        confirmInput = input("Confirm account deletion? (Y/N): ").upper()
                        if confirmInput == "Y":
                            self.delete_account(self.menu.get_user())
                            self.menu.set_user(None)
                            break
                        elif confirmInput == "N":
                            print("Deletion cancelled, returning to menu.")
                            break
                        else:
                            print("Invalid input.")
                    