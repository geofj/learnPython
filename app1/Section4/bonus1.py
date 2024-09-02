# More examples with for-loop

# For loops run in a similar repetitive process to while loops
# Unlike while loops, for-loop depends on the number of items in the list that's referenced

meals = ["pasta", "pizza", "salad"]
# list contains three strings

for meal in meals:
    print(meal.capitalize())
    # the four loop will print each string in the list of meals until all strings have printed

for char in 'meals':
    print(char.capitalize())
    # this for-loop will process the string 'meals' and capitalize each character

print("Bye!")
# this print function will not execute until the for-loop has completely finished executing