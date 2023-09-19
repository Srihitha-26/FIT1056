user_data = "user_data.txt"


# to register a new user (young learner)
def register_user(username, password):
    """
    Registers a new user by adding their username and password to the user data file.

    :param username: The username chosen by the user for their account.
    :param password: The password chosen by the user for their account.
    :return: None
    """

    with open(user_data, "a") as file:
        file.write(f"{username}, {password}\n")


def is_username_taken(username):
    with open(user_data, "r") as file:
        for line in file:
            existing_username, _ = line.strip().split(",")
            if existing_username == username:
                return True
    return False


def login_user(username, password):
    with open(user_data, "r") as file:
        for line in file:
            existing_username, existing_password = line.strip().split(",")
            if existing_username == username and existing_password == password:
                return True
    return False


def user_registration():
    while True:
        username = input("Enter a username: ")
        if is_username_taken(username):
            print("Username is already taken. Please choose another.")
        else:
            break

    password = input("Enter a password: ")
    register_user(username, password)
    print("Registration successful!")


# User Login
def user_login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if login_user(username, password):
            print(f"Welcome, {username}!")
            break
        else:
            print("Invalid username or password. Please try again.")

# def user_login(username, password):  # Add arguments here
#     while True:
#         if login_user(username, password):
#             print(f"Welcome, {username}!")
#             break
#         else:
#             print("Invalid username or password. Please try again.")



# # Function to delete a user account
# def delete_user_account(username):
#     # Read the existing user data from the file
#     with open(user_data, "r") as file:
#         lines = file.readlines()
#
#     # Create a new list of lines without the user's data
#     new_lines = []
#     user_found = False
#     for line in lines:
#         existing_username, _ = line.strip().split(",")
#         if existing_username != username:
#             new_lines.append(line)
#         else:
#             user_found = True
#
#     # If the user was found and their data removed, update the file
#     if user_found:
#         with open(user_data, "w") as file:
#             file.writelines(new_lines)
#         return True  # Account successfully deleted
#     else:
#         return False  # User not found
#
#
# # Example usage to delete a user account
# def delete_account():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#
#     if login_user(username, password):
#         if delete_user_account(username):
#             print("Account successfully deleted.")
#         else:
#             print("Account not found. Deletion failed.")
#     else:
#         print("Invalid username or password. Deletion failed.")

# User deletion function usage
# delete_account()
