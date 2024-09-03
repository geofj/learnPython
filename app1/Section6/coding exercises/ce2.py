# We have a list of two IPs in the code area.
#
# Extend the code so your program:
#
# 1. Prompts the user to input an index (e.g., 0 or 1).
#
# 2. Depending on the user input, the program should return either You chose 100.122.133.111 or You chose 100.122.133.111
#
# Note: In order for the system to mark your exercise as correct, your code should return the exact output
# (i.e., upper case Y in You chose and no spaces or other characters after the IP.
#
# For example:

# Enter the index of the IP you want: 1
# You chose 100.122.133.111

ips = ['100.122.133.105', '100.122.133.111']

assign = int(input("Enter the index (0 or 1) of the IP you want: "))
# takes user input and converts to integer
print(f"You chose {ips[assign]}")
# calls the index from ips list using the integer from user input
