# Create a list view of the todos and have an exit option for program using match-case.
# Show the list in a vertical format - use a for-loop in this situation.
# Create a strip function for the first user input.

todos = []
# empty list to store todos to be printed

while True:
# creates a loop operation based on the True boolean
    start_action = input("Would you like to add, show, display or exit: ")
    # user input of 'add', 'show', display, or exit to guide the user into a match case for either options
    start_action = start_action.strip()
    # strip function allows accidental whitespace after the start user input

    match start_action:
        case 'add':
        # first case 'add' results in user entering to do item and appending the item to todos list
            todo = input("Enter a todo: ")
            # input variable calls the user_prompt string
            todos.append(todo)
            # append function appends the input into the empty todos list
        case 'show' | 'display':
        # second case or display, thanks to ( | bitwise operator) will show the newly appended list
            for item in todos:
            # added a for loop
                item = item.capitalize()
                # capitalizes the to do entries
                print(item)
                # prints the newly appended todos list through the for-loop
        case 'exit':
        # third case will exit the loop
            break
            # exit the loop
        case _:
        # fourth case will catch unknown user entries and guide them back to the loop
            print("You've entered an unknown choice. Please try again.\n")
            # prints guide message

print("Thanks for using the todo list. Bye!")
# good bye message
