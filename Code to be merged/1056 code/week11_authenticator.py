"""
FIT1056 Problem Solving Tasks for Week 11
"""

# Local application imports
from week11_user import User
from week11_patient import Patient


class Authenticator:

    def __init__(self, file_path="./data/week11_users.txt"):
        self.file_path = file_path
        self.users = []
        self.load_users()

    def load_users(self):
        """
        Load list of users from the ./data/users.txt file
        :return: bool (True if successful, False otherwise)
        """
        try:
            with open(self.file_path, "r", encoding="utf8") as users_f:
                users_lines = users_f.readlines()
                for line in users_lines:
                    (username,
                     password,
                     role,
                     is_active,
                     first_name,
                     last_name) = line.strip().split(",")
                    if role == "PA":
                        user_obj = Patient(username=username,
                                           password=password,
                                           is_active=bool(is_active),
                                           first_name=first_name,
                                           last_name=last_name)
                    else:
                        user_obj = User(username=username,
                                        password=password,
                                        role=role,
                                        is_active=bool(is_active))
                    self.users.append(user_obj)
            return True
        except FileNotFoundError:
            print(f"The file \"{self.file_path}\" does not exist!")
            return False

    def authenticate(self, input_username, input_password):
        """
        Logic for authenticating a login procedure
        :param input_username: str - username entered by the user
        :param input_password: str - password entered by the user
        :return: bool
        """
        for user_obj in self.users:
            if user_obj.get_username() == input_username:
                # If username is found
                if (user_obj.get_password() == input_password
                        and user_obj.get_is_active()):
                    # Passwords match and account is active
                    return user_obj
                else:
                    # Authentication fails or account is no longer active
                    return False
        # Account does not exist
        return False


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
