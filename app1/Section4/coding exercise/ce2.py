# Complete the code by adding a for-loop that makes the program produce the following output:

# John Smith
# Sen Plakay
# Dora Ngacely

names = ["john smith", "sen plakay", "dora ngacely"]
# list of the names to display

for name in names:
    name = name.title()
    print(name)
    # for-loop displays the names from our list and capitalizes every first letter of the word (title function)