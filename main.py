# This is a sample Python script.
from user_registration import user_registration, user_login, login_user
from account_deletion import delete_account

while True:
    print("\nWelcome to CodeVenture!")
    print("1. Register")
    print("2. Login")
    print("3. Delete account")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_registration()
    elif choice == "2":
        user_login()
    elif choice == "3":
        delete_account()
    elif choice == "4":
        print("Goodbye! Thank you using CodeVenture")
        break
    else:
        print("Invalid choice. Please try again.")
