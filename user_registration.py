import re

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


def is_valid_password(password):
    min_length = 8
    have_spl_char = re.search(r'[!@#$%&*~]', password) is not None

    if len(password) < min_length:
        return False, "Password must be at least 8 characters long."
    elif not have_spl_char:
        return False, "Password must contain at least one special character."
    else:
        return True, "Your password has been set"


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
    while True:
        password = input("Enter a password: ")
        is_valid, message = is_valid_password(password)
        if is_valid:
            break
        else:
            print(f"Invalid password: {message}")

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