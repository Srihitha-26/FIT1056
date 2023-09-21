import random

class User():
    typeList = ["DEV", "INV", "EDU", "STU"]
    availableTypes = ["Investor", "Educator", "Student"]

    def __init__(self, username: str, password: str, email: str):
        self.set_username(username)
        self.set_password(password)
        self.set_email(email)
        self.userType: str
        

    def set_username(self,newUsername: str) -> bool:
        if newUsername == None:
            print("Username is not entered.")
            return False
        
        elif len(newUsername) > 16:
            print("Username is too long.")
            return False
        
        elif len(newUsername) < 3:
            print("Username is too short.")
            return False
        
        else:
            self.username = newUsername
            return True

    def set_password(self,newPassword: str) -> bool:
        if newPassword == None:
            print("Username is not entered.")
            return False
        
        elif len(newPassword) < 5:
            print("Password is too short")
            return False
        
        else:
            self.password = newPassword
            return True
        
    def set_email(self, newEmail: str) -> bool:
        if newEmail == None:
            return False
        elif not "@" in newEmail:
            return False
        else:
            self.email = newEmail
            return True
    def set_type(self, newType: str) -> bool:
        if newType == None:
            return False
        elif newType not in self.typeList:
            return False
        else:
            self.userType = newType
            return True

    def generate_id(self,idList: list[str]) -> None:
        id1 = self.username[0:3].upper()
        id2 = random.randint(1000,9999)
        while True:
            if f"{id1}[{id2}]" not in idList:
                self.userID = f"{id1}[{id2}]"
                break
            else:
                id2 = random.randint(1000,9999)

    def get_username(self) -> str:
        return self.username
    
    def get_password(self) -> str:
        return self.password
    
    def get_email(self) -> str:
        return self.email
    
    def get_id(self) -> str:
        return self.userID
    
    def get_type(self) -> str:
        return self.userType
    
    def __str__(self) -> str:
        ret = f"\nUsername: {self.username}"
        ret += f"\nUser email: {self.email}"
        ret += f"\nUser ID: {self.userID}"
        return ret

class Investor(User):
    def __init__(self, username: str, password: str, email: str, shares: float):
        super().__init__(username, password, email)
        self.set_shares(shares)
        self.set_type("INV")

    def set_shares(self, newShares: float) -> bool:
        if newShares < 0 or newShares > 100:
            print("Shares must be a number between 0 - 100")
            return False
        else:
            self.shares = newShares
            return True
    
    def __str__(self) -> str:
        ret = super.__str__()
        ret += f"\nShares: {self.shares}%"
        return ret


class Developer(User):
    def __init__(self, username: str, password: str, email: str, workingTimes: list[str]):
        super().__init__(username, password, email)
        self.set_times(workingTimes)
        self.set_type("DEV")

    def set_times(self,newTimes: list[str]) -> bool:
        for i in newTimes:
            try:
                (hours,minutes) = i.split(":")
                hoursCheck = int(hours) > 23 or int(hours) < 0
                minutesCheck = int(minutes) > 59 or int(hours) < 0
            except ValueError:
                print(f"Item {i} is not a valid time.")
                return False
            if hoursCheck or minutesCheck:
                print(f"Item {i} is not a valid time.")
                return False
            elif len(newTimes) != 2:
                print("There must be only two times in the list")
                return False
        self.workingTimes = newTimes
        return True
    
    def get_times(self):
        return self.workingTimes

    def __str__(self) -> str:
        ret = super.__str__()
        ret += f"\n{self.workingTimes[0]} - {self.workingTimes[1]}"
        return ret

class Educator(User):
    def __init__(self, username: str, password: str, email: str, schoolAssociation: str):
        super().__init__(username, password, email)
        self.set_school(schoolAssociation)
        self.set_type("EDU")
    
    def set_school(self, newSchool: str) -> bool:
        if newSchool == None:
            print("School is invalid")
            return False
        else:
            self.schoolAssociation = newSchool
            return True
        
    def __str__(self) -> str:
        ret = super.__str__()
        ret += f"\nSchool Associated: {self.schoolAssociation}"
        return ret


class Student(User):
    def __init__(self, username: str, password: str, email: str, **kwargs):
        super().__init__(username, password, email)
        self.set_type("STU")
        self.schoolAssociation = None
        self.educator = None
        if 'schoolAssociation' in kwargs:
            self.set_school(kwargs['schoolAssociation'])
        if 'educator' in kwargs:
            self.set_educator(kwargs['educator'])

    def set_school(self, newSchool: str) -> bool:
        if newSchool == None:
            print("School is invalid")
            return False
        else:
            self.schoolAssociation = newSchool
            return True

    def set_educator(self, newEducator: Educator) -> bool:
        if newEducator == None or not isinstance(newEducator, Educator):
            print("Educator is invalid")
            return False
        else:
            self.educator = newEducator
            return True
        
    def __str__(self) -> str:
        ret = super.__str__()
        if not (self.schoolAssociation == None):
            ret += f"\nSchool Associated: {self.schoolAssociation}"
        if self.educator is not None:
            ret += f"\nEducator: {self.educator.get_username()}"
        return ret