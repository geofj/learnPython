# Storing user input using python methods

user_prompt = "Enter a todo: "
# variable user_prompt holds the string

todos = []
# empty list to store todos to be printed

while True:
# creates a loop operation based on the True boolean
    todo = input(user_prompt)
    # input variable calls the user_prompt string
    todos.append(todo)
    # append function appends the input into the empty todos list
    print(todos)
    # prints the newly appended todos list

