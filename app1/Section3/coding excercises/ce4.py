# Create a program that prompts the user to input their name repeatedly.
# Then, the program repeatedly prints out the name with the first letter capitalized.

while True:
# while loop to repeatedly print the user_name input

    user_name = input("What is your name? ")
    # variable that stores the user name input
    print(user_name.capitalize())
    # prints the stored user name input