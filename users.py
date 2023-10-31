"""
FIT1056 Software Development Phase
Student name: Yong Wen Jian
Student ID: 33561583
Group: MA_FRI_1600_G2
"""


import random
import re

"""
The User class represents all users that are able to use the CodeVenture program
"""
class User():
    ### TODO: **TKINTER NO BLOCK**
    # REPLACE: all set_ functions with the necessary prompts and errors
    """
    A list of types of users that exist
    """
    typeList = ["DEV", "INV", "EDU", "STU"]

    """
    A list of types of users that can be created within the program
    """
    availableTypes = ["Investor", "Educator", "Student"]

    """
    Constructor method for the User class
    :param username: A string representing the username of the user
    :param password: A string representing the password of the user
    :param email: A string representing the email of the user
    :param kwargs['userID']: An optional string type parameter that represents the ID of the user
    """
    def __init__(self, username: str, password: str, email: str, **kwargs):
        # Setting all data of the user
        self.set_username(username)
        self.password = password
        self.set_email(email)
        # Checking if user ID is provided
        if 'userID' in kwargs:
            if not self.set_id(kwargs['userID']):
                self.generate_id() # Executed if provided ID is invalid
        else:
            self.generate_id()

        self.userType: str
        
    """
    Sets the username of the user account if all constraints are met
    :param newUsername: A string representing the new username to be set
    :return: A boolean representing if the new username is set successfully
    """
    def set_username(self,newUsername: str) -> bool:
        # if-elif-else block to verify that newUsername is a valid username to be set
        if newUsername == None:
            print("Username is not entered.")
            return False
        
        elif len(newUsername) > 16:
            print("Username is too long.")
            return False
        
        elif len(newUsername) < 3:
            print("Username is too short.")
            return False
        
        else: # Executed if username is valid
            self.username = newUsername
            return True

    """
    Sets the password of the user account if all constraints are met
    :param newPassword: A string representing the new password to be set on the account
    :return: A boolean representing if the new password is set successfully
    """
    def set_password(self,newPassword: str) -> bool:
         # Int representing the minimum length of the password
        min_length = 8

        # Boolean representing if newPassword has symbols
        have_spl_char = re.search(r'[!@#$%&*~]', newPassword) is not None 

        # if-elif-else block to verify that newPassword is a valid password to be set
        if newPassword == None:
            print("Password is invalid.")
            return False
        
        elif len(newPassword) < min_length:
            print("Password must be at least 8 characters long.")
            return False
        
        elif not have_spl_char:
            print("Password must contain at least one special character.")
            return False
        
        else: # Executed if password is valid
            self.password = newPassword
            return True

    """
    Sets the email of the user account if all constraints are met
    :param newEmail: A string representing the new email to be set on the account
    :return: A boolean representing if the new email is set successfully
    """    
    def set_email(self, newEmail: str) -> bool:
        # if-elif-else block to verify that newEmail is a valid email to be set
        if newEmail == None:
            return False
        
        elif not "@" in newEmail:
            return False
        
        else: # Executed if email is valid
            self.email = newEmail
            return True
    
    """
    Sets the type of the user account if all constraints are met
    :param newType: A string representing the new type to be set on the account
    :return: A boolean representing if the new type is set successfully
    """    
    def set_type(self, newType: str) -> bool:
        # if-elif-else block to verify that newEmail is a valid email to be set
        if newType == None:
            return False
        
        elif newType not in self.typeList:
            return False
        
        else: # Executed if the given type is valid
            self.userType = newType
            return True
    
    """
    Sets the ID of the user account if all constraints are met
    :param newID: A string representing the new ID to be set on the account
    :return: A boolean representing if the new ID is set successfully
    """
    def set_id(self, newID: str) -> bool:
        # if-else block to verify that newEmail is a valid email to be set
        if newID == None:
            return False
        
        else: # Executed if the given ID is valid
            self.userID = newID
            return True

    """
    Generates the ID of the user account if all constraints are met
    :param idList: A list of strings representing all currently existing ids
    :return: None
    """
    def generate_id(self,idList: list[str]) -> None:
        id1 = self.username[0:3].upper()
        id2 = random.randint(1000,9999)
        # Checking if generated ID is in list, regenerate if it is.
        while True:
            if f"{id1}[{id2}]" not in idList:
                self.userID = f"{id1}[{id2}]"
                break
            else:
                id2 = random.randint(1000,9999)

    """
    Getter method for the username of the user account
    :return: A string representing the username of the account
    """
    def get_username(self) -> str:
        return self.username
    
    """
    Getter method for the password of the user account
    :return: A string representing the password of the account
    """
    def get_password(self) -> str:
        return self.password
    
    """
    Getter method for the email of the user account
    :return: A string representing the email of the account
    """
    def get_email(self) -> str:
        return self.email
    
    """
    Getter method for the ID of the user account
    :return: A string representing the ID of the account
    """
    def get_id(self) -> str:
        return self.userID
    
    """
    Getter method for the type of user account
    :return: A string representing the type of account
    """
    def get_type(self) -> str:
        return self.userType
    
    """
    Magic method that converts the User instance to a string
    :return: A string representing the details of the User instance
    """
    def __str__(self) -> str:
        ret = f"\nUsername: {self.username}"
        ret += f"\nUser email: {self.email}"
        ret += f"\nUser ID: {self.userID}"
        return ret

    """
    A method that concatenates the user data in a way where it is stored to the database.
    """
    def to_database(self) -> str:
        return f"{self.get_username()},{self.get_password()},{self.get_email()},{self.get_type()},{self.get_id()}"

"""
The Developer class represents all developers that are able to use the CodeVenture program
"""
class Developer(User):
    """
    Overrides __init__ method in User class, functionality remains the same.
    """
    def __init__(self, username: str, password: str, email: str, workingTimes: list[str], **kwargs):
        if 'userID' in kwargs:
            super().__init__(username, password, email, userID=kwargs['userID'])
        else:
            super().__init__(username, password, email)
        self.set_times(workingTimes)
        self.set_type("DEV")

    """
    Sets the working times of the developer if all constraints are met
    :param newTimes: A list of strings representing the new working times to be set on the account
    :return: A boolean representing if the new working times is set successfully
    """
    def set_times(self,newTimes: list[str]) -> bool:
        # Checking both times in the list
        for i in newTimes:

            # try-except block to verify that newTimes is a valid working time to be set
            try:
                (hours,minutes) = i.split(":")
                hoursCheck = int(hours) > 23 or int(hours) < 0
                minutesCheck = int(minutes) > 59 or int(hours) < 0
            except ValueError:
                print(f"Item {i} is not a valid time.")
                return False
            
            # if-elif-else block to verify that newTimes is a valid working time to be set
            if hoursCheck or minutesCheck:
                print(f"Item {i} is not a valid time.")
                return False
            elif len(newTimes) != 2:
                print("There must be only two times in the list")
                return False

        # If nothing returns false, new working times are set
        self.workingTimes = newTimes
        return True
    
    """
    Getter method for the working times of the developer
    :return: A list of strings representing the working times of the developer
    """
    def get_times(self) -> list[str]:
        return self.workingTimes

    """
    Overrides __str__ method in User class, functionality remains the same.
    """
    def __str__(self) -> str:
        ret = super().__str__()
        ret += f"\nWorking times: {self.workingTimes[0]} - {self.workingTimes[1]}\n"
        return ret
    
    """
    Overrides to_database method in User class, functionality remains the same.
    """
    def to_database(self) -> str:
        return f"{super().to_database()},{self.get_times()[0]},{self.get_times()[1]}\n"
    
"""
The Investor class represents all investors that are able to use the CodeVenture program
"""
class Investor(User):
    """
    Overrides __init__ method in User class, functionality remains the same.
    """
    def __init__(self, username: str, password: str, email: str, shares: float, **kwargs):
        if 'userID' in kwargs:
            super().__init__(username, password, email, userID=kwargs['userID'])
        else:
            super().__init__(username, password, email)
        self.set_shares(shares)
        self.set_type("INV")

    """
    Sets the shares of the investor account if all constraints are met
    :param newShares: A float representing the new amount of shares to be set on the account
    :return: A boolean representing if the new amount of shares is set successfully
    """
    def set_shares(self, newShares: float) -> bool:
        # if-else block to check the validity of the shares
        if newShares < 0 or newShares > 100:
            print("Shares must be a number between 0 - 100")
            return False
        
        else: # Executed if the amount of shares is valid
            self.shares = newShares
            return True

    """
    Getter method for the shares of the investor account
    :return: A float representing the shares held within the account
    """
    def get_shares(self) -> float:
        return self.shares
    
    """
    Overrides __str__ method in User class, functionality remains the same.
    """
    def __str__(self) -> str:
        ret = super().__str__()
        ret += f"\nShares: {self.shares}%\n"
        return ret
    
    """
    Overrides to_database method in User class, functionality remains the same.
    """
    def to_database(self) -> str:
        return f"{super().to_database()},{self.get_shares()}\n"

"""
The Educator class represents all educators that are able to use the CodeVenture program
"""
class Educator(User):
    """
    Overrides __init__ method in User class, functionality remains the same.
    """
    def __init__(self, username: str, password: str, email: str, schoolAssociation: str, **kwargs):
        if 'userID' in kwargs:
            super().__init__(username, password, email, userID=kwargs['userID'])
        else:
            super().__init__(username, password, email)
        self.set_school(schoolAssociation)
        self.set_type("EDU")
    
    """
    Sets the school of the educator account if all constraints are met
    :param newSchool: A string representing the new school to be set on the account
    :return: A boolean representing if the new school is set successfully
    """
    def set_school(self, newSchool: str) -> bool:
        # If-else block to check for the validity of newSchool as a school
        if newSchool == None:
            print("School is invalid")
            return False
        
        else: # Executed if newSchool is a valid school
            self.schoolAssociation = newSchool
            return True

    """
    Getter method for the school of the account
    :return: A string representing the school associated the account
    """    
    def get_school(self) -> str:
        return self.schoolAssociation

    """
    Overrides __str__ method in User class, functionality remains the same.
    """    
    def __str__(self) -> str:
        ret = super().__str__()
        ret += f"\nSchool Associated: {self.schoolAssociation}\n"
        return ret
    
    """
    Overrides to_database method in User class, functionality remains the same.
    """
    def to_database(self) -> str:
        return f"{super().to_database()},{self.get_school()}\n"

"""
The Student class represents all students that are able to use the CodeVenture program
"""
class Student(User):
    """
    Overrides __init__ method in User class, functionality remains the same.
    """
    def __init__(self, username: str, password: str, email: str, schoolAssociation: str, educator: Educator, **kwargs):
        if 'userID' in kwargs:
            super().__init__(username, password, email, userID=kwargs['userID'])
        else:
            super().__init__(username, password, email)
        self.set_type("STU")
        self.schoolAssociation = None
        self.educator = None
        self.set_school(schoolAssociation)
        self.set_educator(educator)

    """
    Sets the school of the student account if all constraints are met
    :param newSchool: A string representing the new school to be set on the account
    :return: A boolean representing if the new school is set successfully
    """
    def set_school(self, newSchool: str) -> bool:
        # If-else block to check for the validity of newSchool as a school
        if newSchool != None and not isinstance(newSchool, str):
            print("School is invalid")
            return False
        
        else: # Executed if newSchool is a valid school
            self.schoolAssociation = newSchool
            return True

    """
    Sets the educator of the student account if all constraints are met
    :param newEducator: An Educator instance representing the new educator to be set on the student's account
    :return: A boolean representing if the new educator is set successfully
    """
    def set_educator(self, newEducator: Educator) -> bool:
        # If-else block to check for the validity of newEducator as a educator
        if newEducator != None and not isinstance(newEducator, Educator):
            print("Educator is invalid")
            return False
        
        else: # Executed if newEducator is a valid educator instance
            self.educator = newEducator
            return True

    """
    Getter method for the school of the account
    :return: A string representing the school associated the account
    """    
    def get_school(self) -> str:
        return self.schoolAssociation
    
    """
    Getter method for the educator of the account
    :return: An Educator instance representing the educator associated the account
    """
    def get_educator(self) -> Educator:
        return self.educator

    """
    Overrides __str__ method in User class, functionality remains the same.
    """    
    def __str__(self) -> str:
        ret = super().__str__()
        if not (self.schoolAssociation == None):
            ret += f"\nSchool Associated: {self.schoolAssociation}"
        if not (self.educator == None):
            ret += f"\nEducator: {self.get_educator().get_username()}\n"
        return ret
    
    """
    Overrides to_database method in User class, functionality remains the same.
    """
    def to_database(self) -> str:
        return f"{super().to_database()},{self.get_school()},{self.get_educator().get_username()}\n"