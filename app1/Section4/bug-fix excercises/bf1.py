# The programmer is trying to loop over the buttons list and print out each item with the first letter capitalized.
# However, the programmer has done something wrong. Try to find and fix the issue.
# code below:

# for i in buttons:
#     print(i.capitalize())
#
# buttons = ["cancel", "reply", "submit"]

buttons = ["cancel", "reply", "submit"]
# moved buttons variable and list before the for-loop, allowing the list to be printed successfully

for i in buttons:
    print(i.capitalize())

