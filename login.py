"""
FIT1056 Software Development Phase
Student name: Yong Wen Jian
Student ID: 33561583
Group: MA_FRI_1600_G2
"""


from menu import Menu
from users import *
from game import *
from modulehandler import ModuleHandler
from feedback import FeedbackAction
import os
from msvcrt import getch
import getpass, sys


class Login:
    """
    The login class represents the class that provides the options for a user to login and operate the functions within CodeVenture
    """
    
    menu = Menu()
    """
    A menu instance to be used to display the main menus
    """

    game = Game()
    """
    A game instance to be used by students to run CodeVenture
    """

    feedback = FeedbackAction()
    """
    A FeedbackAction instance to be used by users to provide feedback
    """

    modulehandler = ModuleHandler()

    baseFile = os.path.dirname(os.path.realpath('__file__'))
    """
    A string representing the directory to the current file
    """

    devsData = os.path.join(baseFile,'database\devs.txt')
    """
    A string representing the path to the developer data file
    """

    invsData = os.path.join(baseFile,'database\invs.txt')
    """
    A string representing the path to the investor data file
    """

    edusData = os.path.join(baseFile,'database\edus.txt')
    """
    A string representing the path to the educator data file
    """

    stusData = os.path.join(baseFile,'database\stus.txt')
    """
    A string representing the path to the student data file
    """

    
    def auth_account(self,usernameInput: str, passwordInput: str, accounts: list[list[str]]):
        """
        The method to authenticate an account based on a given username and password
        :param usernameInput: A string representing the user provided username input
        :param passwordInput: A string representing the user provided password input
        :param accounts: A list of lists containing the username and password data for the accounts
        """
        result = False
        
        # Checking each username in accounts
        for i in range(len(accounts)):
            # If accounts match, check the password provided
            if accounts[i][0] == usernameInput:
                # If the passwords match, set the account index in accounts and set result to true
                if accounts[i][1] == passwordInput:
                    self.accountIndex = i
                    result = True
                break
        return result

    
    def create_account(self,accountType: str, allIDs: list[str], allUsernames: list[str], **kwargs) -> User:
        """
        The method to create an account in CodeVenture
        :param accountType: The type of account to be created
        :param allIDs: A list of IDs for every single user
        :param allUsernames: A list of usernames for every single user
        """
        # Start with a new User instance where each variable can be replaced
        newUser = User("Placeholder","Placeholder","Placeholder@email.nul")

        ### TODO: Replace with **TKINTER** stuff ###
        ### Base account creation block ###
        # Prompt to set the username of the account
        while True:
            # REPLACE: with textline
            usernameInput = input("\nPlease enter a username: ")
            if newUser.set_username(usernameInput):
                if newUser.get_username() not in allUsernames: # Make sure the username does not already exist
                    break
                else:
                    print("Username has been taken.")

        # Prompt to set the password of the account
        while True:
            # REPLACE: with textline which is masked, should give *****
            passwordInput = self.mask_password("\nPlease enter your password: ")
            if newUser.set_password(passwordInput):
                break

        # Prompt to set the email of the account
        while True:
            # REPLACE: with text line
            emailInput = input("\nPlease enter your email: ")
            if newUser.set_email(emailInput):
                break

        # Regenerate the ID once all base data have been given
        newUser.generate_id(allIDs)
        ### End of base account creation block ###

        # Checking for the account type provided and prompt for additional information

        ### TODO: **TKINTER** yes ####
        ### Start of specialized prompt block ###
        match accountType:
            case "Investor":
                # Creating new Investor instance with all previous data
                newUser = Investor(newUser.get_username, newUser.get_password, newUser.get_email, 0, userID=newUser.get_id())

                # Prompt to set shares of the account
                while True:
                    # REPLACE: w/ text box or something that takes a number from 1-100 should work
                    sharesInput = input("\nPlease enter the current amount of shares that is held (%): ")
                    if newUser.set_shares(sharesInput):
                        # Append data once completed
                        with open(self.invsData, "a") as file:
                            file.write(f"{newUser.get_username()},{newUser.get_password()},{newUser.get_email()},{newUser.get_id()},{newUser.get_shares()}")
                            file.close()
                        break

            case "Educator":
                # Creating new Educator instance with all previous data
                newUser = Educator(newUser.get_username, newUser.get_password, newUser.get_email, "exschool", userID=newUser.get_id())
                
                # Prompt to set school of the account
                while True:
                    # REPLACE: w/ text box probably
                    schoolInput = input("\nPlease enter the name of the school that you are teaching at: ")
                    if newUser.set_school(schoolInput):
                        # Append data once completed
                        with open(self.edusData, "a") as file:
                            file.write(f"{newUser.get_username()},{newUser.get_password()},{newUser.get_email()},{newUser.get_id()},{newUser.get_school()}")
                            file.close()
                        break

            case "Student":
                # Creating new Student instance with all previous data
                newUser = Student(newUser.get_username, newUser.get_password, newUser.get_email, userID=newUser.get_id())

                # Prompt to see if the student has a school or educator
                while True:
                    # REPLACE: Button with Y/N, checking if the student has a teacher.
                    educationInput = input("\nAre you a student of an educator for this program? (Y/N): ").upper()
                    
                    # If yes, prompt for educator and school
                    if educationInput == "Y":
                        while True: # Educator prompt
                            # REPLACE: Get name of the educator username, text box probably
                            educatorInput = input("\nPlease enter the username of your educator: ")
                            found = False
                            for i in range(kwargs['edus'][0]): # kwargs['edus'] is a list of all educator data
                                if educatorInput == kwargs['edus'][0][i]:
                                    studentEducator = Educator(kwargs['edus'][0][i], kwargs['edus'][1][i], kwargs['edus'][2][i], kwargs['edus'][4][i], userID=kwargs['edus'][3][i])
                                    newUser.set_educator(studentEducator)
                                    found = True
                                    break
                            if found:
                                break
                            else:
                                # REPLACE: Error, retry.
                                print("Educator username not found in database.") 

                        
                        while True: # School prompt
                            # REPLACE: Get name of the school, text box probably
                            schoolInput = input("\nPlease enter the name of the school that you are learning at: ")
                            if newUser.set_school(schoolInput):
                                # Append data once completed
                                with open(self.stusData, "a") as file:
                                    file.write(f"{newUser.get_username()},{newUser.get_password()},{newUser.get_email()},{newUser.get_id()},{newUser.get_school()},{newUser.get_educator().get_username()}")
                                    file.close()
                                break
                        break
                    
                    # If not, append current data into file
                    elif educationInput == "N":
                        with open(self.stusData, "a") as file:
                            file.write(f"{newUser.get_username()},{newUser.get_password()},{newUser.get_email()},{newUser.get_id()},None,None")
                            file.close()
                        break

                    else:
                        # REPLACE: Can probably be removed if a Y/N button is used, since this relies on the reply not being Y nor N
                        print("Invalid Input.")

            case _: # Case if somehow no types have matched
                # REPLACE: Error box if no account type (educator, student, investor) has matched
                print("No account type matched")
                return None
        ### End of specialized creation block ###

        # Returns newUser instance once account is made
        return newUser
    
    
    def delete_account(self,user: User):
        """
        Method for user to delete their own account
        """
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


    ### TODO: ?***TKINTER***? ###
    # This function masks the password, not sure if it can be replaced since this is terminal based
    ### Mask password block ###
    def mask_password(prompt: str ="Please enter your password: ") -> str:
        """
        Prompt for a password and masks the input.
        :param prompt: A string working as a prompt for the user similar to input() 
        :return: A string entered by the user.
        """

        if sys.stdin is not sys.__stdin__:
            pwd = getpass.getpass(prompt)
            return pwd
        else:
            pwd = ""        
            sys.stdout.write(prompt)
            sys.stdout.flush()        
            while True:
                key = ord(getch())
                if key == 13: # Return Key
                    sys.stdout.write('\n')
                    return pwd
                    break
                if key == 8: # Backspace key
                    if len(pwd) > 0:
                        # Erases previous character.
                        sys.stdout.write('\b' + ' ' + '\b')                
                        sys.stdout.flush()
                        pwd = pwd[:-1]                    
                else:
                    # Masks user input.
                    char = chr(key)
                    sys.stdout.write('*')
                    sys.stdout.flush()                
                    pwd = pwd + char

    ### End of mask password block ###
    
    """
    Main login method for users to interact with the menu andd browse around CodeVenture
    :return: None
    """
    def login_main(self):
        # Getting all devs data
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

        # Getting all investor data
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

        # Getting all educator data
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

        # Getting all student data
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

        # Creating a list of all usernames and IDs to be used for account creation
        allUsernames = [devUsernames, invUsernames, eduUsernames, stuUsernames]
        allIDs = [devIDs, invIDs, eduIDs, stuIDs]

        # While true loop to keep the program running
        while True:
            # Print and get the option selected from the main menu
            selectedOption = self.menu.option_select(self.menu.main_menu())

            # Match each selection to each case to run the corresponding functions
            match selectedOption:

                ### TODO: **TKINTER** ###
                ### Login block ###
                case "Log In": # User decides to log in
                    # REPLACE: Username and password input (mask pw)
                    usernameInput = input("\nPlease enter your username: ")
                    passwordInput = self.mask_password("\nPlease enter your password: ")
                

                    # Go through authentication for each type of user, sets the menu user if the user is found
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
                    
                    # Executed if account is not found
                    else: 
                        # REPLACE: Error, account not found
                        print("Invalid account username or password, returning to menu.")

                ### End of login block ###

                case "Create Account": # User decides to make an account
                    typeOption = self.menu.option_select(self.menu.create_account_type_menu(User.availableTypes))
                    self.menu.set_user(self.create_account(typeOption, allIDs, allUsernames, edus=[eduUsernames,eduPasswords,eduEmails,eduIDs,eduSchools]))
                    

                case "Exit Program": # User decides to stop using CodeVenture
                    print("Exiting program...")
                    break

                case "View Shares": # Investor decides to view shares
                    print(f"Shares: {self.menu.get_user().get_shares()}%")

                ### TODO: **TKINTER** ###
                ### Buying/Selling shares block ###
                case "Buy Shares": # Investor decides to buy shares
                    print(f"Current Shares: {self.menu.get_user().get_shares()}%")

                    
                    # Prompt for shares input
                    while True:
                        try:
                            # REPLACE: Getting a float number input
                            sharesInput = float(input("\nPlease enter the percentage(%) of shares to buy: "))
                        except ValueError:
                            # REPLACE: Error, not a number, or can just remove if there is a number input
                            print("Invalid amount of shares.")
                        
                        # Checking if the bought shares exceeds threshold or is negative.
                        if sharesInput > (100 - self.menu.get_user().get_shares()):
                            # REPLACE: Error, too many shares
                            print("Owned shares cannot surpass 100%")
                        elif sharesInput < 0:
                            # REPLACE: Error, negative shares
                            print("Cannot buy negative shares")

                        # If shares is valid, it is bought
                        else:
                            self.menu.get_user().set_shares(sharesInput + self.menu.get_user().get_shares())
                            # REPLACE: Success!
                            print(f"Bought {sharesInput}% of shares.")
                            break

                case "Sell Shares": # Investor decides to sell shares
                    print(f"Current Shares: {self.menu.get_user().get_shares()}%")

                    # Prompt for shares input
                    while True:
                        try:
                            # REPLACE: Getting a float number input
                            sharesInput = float(input("\nPlease enter the percentage(%) of shares to sell: "))
                        except ValueError:
                            # REPLACE: Error, not a number, or can just remove if there is a number input
                            print("Invalid amount of shares.")
                        
                        # Checking if the sold shares exceeds threshold or is negative.
                        if sharesInput > self.menu.get_user().get_shares():
                            # REPLACE: Error, too many shares
                            print("Sold shares cannot surpass owned shares.")
                        elif sharesInput < 0:
                            # REPLACE: Error, negative shares
                            print("Cannot sell negative shares")
                            
                        # If shares is valid, it is sold
                        else:
                            self.menu.get_user().set_shares(self.menu.get_user().get_shares() - sharesInput)
                            # REPLACE: Success!
                            print(f"Sold {sharesInput}% of shares.")
                            break

                ### End of buying/selling shares block ###

                case "Set New Working Times": # Developer decides to change working times
                    ### TODO: **TKINTER** ###
                    ### Working times block ###

                    # REPLACE: printing current working times
                    print(f"Current working times: {self.menu.get_user().get_times()[0]} - {self.menu.get_user().get_times()[1]}")

                    # REPLACE: Prompt for new working times
                    while True:
                        startInput = input("Set new starting time (HH:MM): ")
                        endInput = input("Set new ending time (HH:MM): ")
                        if self.menu.get_user().set_times([startInput, endInput]): # Checking if times are set
                            break
                    ### End of working times block ###

                case "View Feedback": # Developer decides to view all feedback
                    self.feedback.read()

                case "Add Module": # Educator decides to add a new module
                    self.modulehandler.create_module()

                case "Remove Module": # Educator decides to remove a module
                    key = self.modulehandler.pick_module()
                    self.modulehandler.remove_module(key)

                case "Add Quizzes": # Educator decides to create a quiz
                    key = self.modulehandler.pick_module()
                    self.modulehandler.create_code_quiz(key)
                
                case "Remove Quizzes": # Educator decides to remove a quiz
                    key = self.modulehandler.pick_module()
                    self.modulehandler.remove_code_quiz(key)
                
                case "Attempt Module": # Student decides to play the quizzes
                    key = self.game.pick_module()
                    mcqPoints = self.game.attempt_mcq_quizzes(key)
                    codePoints = self.game.attempt_code_quizzes(key)
                
                ### TODO: **TKINTER** ###
                ### Education stuff block ###
                case "Change Associated School": # Educator/Student decides to change school names
                    # REPLACE: Prompt for new school input
                    while True:
                        schoolInput = input("Please enter the new school name: ")
                        if self.menu.get_user().set_school(schoolInput):
                            break

                case "Set Educator": # Student decides to set new educator
                    # REPLACE: Prompt for educator username
                    while True:
                        educatorInput = input("\nPlease enter the username of your educator: ")
                        found = False
                        for i in range(eduUsernames):
                            if educatorInput == eduUsernames: # Setting new student educator instance if educator is found
                                studentEducator = Educator(eduUsernames[i], eduPasswords[i], eduEmails[i], eduSchools[i], userID=eduIDs[i])
                                if self.menu.get_user().set_educator(studentEducator):
                                    found = True
                                    break
                        if found:
                            break

                        # Executed if educator username is not found in database
                        else:
                            # REPLACE: Error, educator not found
                            print("Educator not found.")
                ### End of education stuff block ###

                case "Provide Feedback": # User wishes to provide feedback
                    self.feedback.write()

                case "View Profile": # User decides to view their profile
                    ### TODO: **TKINTER NO BLOCK** ###
                    # REPLACE: Printing the entire user profile, they have a __str__ function.
                    print(str(self.menu.get_user()))
                
                ### TODO: **TKINTER** ###
                ### Change pass block ###
                case "Change Password": # User decides to change their password
                    tries = 0
                    passed = False
                    # REPLACE: Prompt for old password (masked)
                    while True:
                        oldPass = self.mask_password("Please enter the current password: ")
                        if oldPass == self.menu.get_user().get_password():
                            passed = True
                            break
                        else:
                            tries += 1
                            # REPLACE: Error, retry
                            print("Password is incorrect")
                            if tries > 2: # Executed if too many tries are done
                                # REPLACE: Error, return to menu
                                print("Tries exceeded, returning to menu.")
                                break
                    
                    # If correct password is entered, prompt to set a new password
                    while passed:
                        # REPLACE: Prompt for new pass (masked)
                        newPass = self.mask_password("Please enter the new password: ")
                        if self.menu.get_user().set_password(newPass): # Prompt to enter new password again to confirm
                            # REPLACE: Prompt for re-entering new pass (masked)
                            confirmPass = self.mask_password("Please re-enter the new password: ")
                            if self.menu.get_user().get_password() == confirmPass:
                                # REPLACE: Success!
                                print("New password set.")
                                break
                            else: 
                                # REPLACE: Return to entering a new password if the confirm password does not match
                                print("Re-entered password does not match the new password.")
                ### End of change pass block ###
                
                case "Log Out": # User chooses to log out
                    print("Saving data.") # Saves all data that may be changed during use
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

                    ### TODO: **TKINTER NO BLOCK** ###
                    # REPLACE: Once all data is saved, log out.
                    print("Logging out.") 
                    self.menu.set_user(None)

                case "Delete Account": # User chooses to delete their own account
                    while True:
                        # REPLACE: Prompt for confirmation
                        confirmInput = input("Confirm account deletion? (Y/N): ").upper()
                        if confirmInput == "Y":
                            self.delete_account(self.menu.get_user()) # Account is deleted if Y is inputted
                            self.menu.set_user(None)
                            break
                        elif confirmInput == "N":
                            # REPLACE: Printing deletion is cancelled
                            print("Deletion cancelled, returning to menu.")
                            break
                        else:
                            # REPLACE: Error, input is not Y or N, can remove if buttons are used
                            print("Invalid input.")
                    