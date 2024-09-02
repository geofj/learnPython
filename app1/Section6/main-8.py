# Add a numbered todos feature using enumerate function

todos = []
# empty list to store todos to be printed

while True:
# creates a loop operation based on the True boolean
    start_action = input("Would you like to add, show, edit or exit: ")
    # user input of 'add', 'show', 'edit' or 'exit' to guide the user into a match case for either options
    start_action = start_action.strip()
    # strip function allows accidental whitespace after the start user input

    match start_action:
        case 'add':
        # first case 'add' results ina for loop user entering to do item and appending the item to todos list
            todo = input("Enter a todo: ")
            # input variable calls the user_prompt string
            todos.append(todo)
            # append function appends the input into the empty todos list
        case 'show':
        # second case will show the newly appended list
            for index, item in enumerate(todos):
            # added an enumerate function to the for-loop to assign numbers to our todos
                print(index, '-', item)
                # prints the newly appended todos list and assigned numbers through the for-loop
        case 'edit':
            number = int(input("Which todo item would you like to to edit: "))
            # int function converts string to a number
            number = number - 1
            # minus 1 to account for 0
            new_todo = input("Enter your new todo: ")
            # input function catches the new to do from user
            todos[number] = new_todo
            # the new to do is now appended to the list
        case 'exit':
        # third case will exit the loop
            break

print("Thanks for using the todo list. Bye!")
# good bye message
