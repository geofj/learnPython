# Create a program that:
#
# 1. Prompts the user to input a (dollar) amount.
#
# 2. Calculates the corresponding amount in euros, given an exchange rate of 2.
#
# 3. Prints out the amount in euros.

rate = 2
# currency conversion rate

amount = float(input("Enter a dollar amount you'd like to convert: "))
# the amount to convert, in dollars is converted to a float
calculate = amount * 2
# to calculate, we use the multiplication operator to multiply our float and the currency rate of 2
print(calculate)
# prints the converted currency