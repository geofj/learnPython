# Create a program where user is asked to enter a password, and check if the password is correct

user_password = input("Please enter your password: ")
# user input to collect password

if user_password != "pass123":
    print("Sorry, that's not the correct password. Please try again later.")
    # if password is not pass123, user will have to re-enter the password

else:
    print("Password was correct! Logging you in now.")
    # if password is pass123, user will be logged in