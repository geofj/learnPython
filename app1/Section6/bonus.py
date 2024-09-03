waiting_list = ["sen", "ben", "john"]
waiting_list.sort()
# as lists are mutable, you can call the sort method without assigning a new variable

for index, i in enumerate(waiting_list):
# enumerate function to number the waiting list
    row = f"{index + 1}.{i.capitalize()}"
    # fstrings to format the text to show "number.name"
    print(row)
    # prints the rows