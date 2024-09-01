# Create a program that prompts the user to input their name once.
# Then, the program *repeatedly* prints out the name once with the first letter capitalized.

user_name = input("Please enter your name: ")
# variable that stores the user name input

while True:
# while loop to repeatedly print the user_name input
    print(user_name.capitalize())
    # prints the stored user name input