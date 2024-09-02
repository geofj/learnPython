# The code below is supposed to print out the items of the list with the first character of each item capitalized.
# However, the code contains two errors. Try to find and fix the errors.
# code below:

# for item in ["sandals", "glasses", "trousers"):
#     print(item.capitalize)

for item in ["sandals", "glasses", "trousers"]:
# lists should always have [ and ], removed the ) at the end
    print(item.capitalize())
    # capitalize function should have ()