
# Function to delete a user account
from user_registration import user_data, login_user, user_login

user_data = "user_data.txt"


def delete_user_account(username):
    # Read the existing user data from the file
    with open(user_data, "r") as file:
        lines = file.readlines()

    # Create a new list of lines without the user's data
    new_lines = []
    user_found = False
    for line in lines:
        existing_username, _ = line.strip().split(",")
        if existing_username != username:
            new_lines.append(line)
        else:
            user_found = True

    # If the user was found and their data removed, update the file
    if user_found:
        with open(user_data, "w") as file:
            file.writelines(new_lines)
        return True  # Account successfully deleted
    else:
        return False  # User not found


# Example usage to delete a user account
def delete_account():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if login_user(username, password):
        if delete_user_account(username):
            print("Account successfully deleted.")
        else:
            print("Account not found. Deletion failed.")
    else:
        print("Invalid username or password. Deletion failed.")
