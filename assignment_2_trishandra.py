#Import the necessary libraries
import json
import os

# Define the file name for storing the user data
assignment_file = "users.json"

def sign_up():
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
    mobile_number = input("Enter Your Mobile Number: ")

    # Create a new user dictonary to store the user data
    user = {
        "username": username,
        "password": password,
        "mobile_number": mobile_number
    }

    # Load the existing database or create a new one if it doesn't exist
    if os.path.exists(assignment_file):
        with open(assignment_file, "r") as f:
            users = json.load(f)
    else:
        users = []

    # Append the new user to the database
    users.append(user)

    # Save the updated database
    with open(assignment_file, "w") as f:
        json.dump(users, f)

    print("User Created Successfully!")

def sign_in():
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")

    # Load the database
    if os.path.exists(assignment_file):
        with open(assignment_file, "r") as f:
            users = json.load(f)
    else:
        print("No Users Found!")
        return

    # Check if the username and password match
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Welcome To The Device!")
            print("Your Phone Number Is:", user["mobile_number"])
            return

    print("Incorrect Credentials!")
    exit()

def main():
    while True:
        print("1. Sign Up")
        print("2. Sign In")
        choice = input("Choose Your Option: ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        else:
            print("Invalid Option, Try Again!")

if __name__ == "__main__":
    main()