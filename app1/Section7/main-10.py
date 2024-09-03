# Getting to do items from the text files

while True:
# creates a loop operation based on the True boolean
    start_action = input("Would you like to add, show, edit, complete or exit: ")
    # user input of 'add', 'show', 'edit' or 'exit' to guide the user into a match case for either options
    start_action = start_action.strip()
    # strip function allows accidental whitespace after the start user input

    match start_action:
        case 'add':
        # first case 'add' results ina for loop user entering to do item and appending the item to todos list
            todo = input("Enter a todo: ") + "\n"
            # input variable calls the user_prompt string
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            # opens the todos.txt file in read mode
            todos.append(todo)
            # append function appends the input into the empty todos list
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            # opens the todos.txt file in write mode
        case 'show':
        # second case will show the newly appended list
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            # opens the todos.txt file in read mode
            for index, item in enumerate(todos):
            # added an enumerate function to the for-loop to assign numbers to our todos
                print(f"{index + 1}-{item}")
                # prints the newly appended todos list and assigned numbers through the for-loop
                # added fstring to format the text without spaces
        case 'edit':
            number = int(input("Which todo item would you like to to edit: ")) - 1
            # int function converts string to a number, minus 1 to account for 0
            new_todo = input("Enter your new todo: ")
            # input function catches the new to do from user
            todos[number] = new_todo
            # the new to do is now appended to the list
        case 'complete':
            complete_item = int(input("Which todo item would you like to mark complete: ")) - 1
            # user input for which to do item to mark complete, input is converted to int to account for 0
            todos.pop(complete_item)
            # pop method is used to remove the index item from the to dos list
        case 'exit':
        # third case will exit the loop
            break

print("Thanks for using the todo list. Bye!")
# goodbye message
