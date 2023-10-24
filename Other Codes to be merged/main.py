# This is a sample Python script.
from track_progress import track_progress
from user_registration import user_registration, user_login


def main():
    progress_tracker = track_progress()
    while True:
        print("\nWelcome to CodeVenture!")
        print("1. Register")
        print("2. Login")
        print("3. Delete account")
        print("4. Check achievements")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_registration()
        elif choice == "2":
            user_login()
        elif choice == "3":
            delete_account()
        elif choice == "4":
            username = input("Enter your username: ")
            password = input("Enter your username: ")
            user_progress = progress_tracker.get_user_progress(username, password)
            if user_progress:
                print(f"User Progress: {user_progress}")
            else:
                print("User not found.")
        elif choice == "5":
            print("Goodbye! Thank you using CodeVenture")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
