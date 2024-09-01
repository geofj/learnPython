# A programmer wrote the following program:

# countries = []
#
# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
# print(countries)

# The expected output is as follows:

# Enter the country: Cambodia
# ['Cambodia']
# Enter the country: Triomindia
# ['Cambodia', 'Triomindia']
# Enter the country:

# However, the code returns an error instead of the expected output.
# Fix the code, so it produces the expected output.

countries = []

while True:
    country = input("Enter the country: ")
    country_cap = country.capitalize()
    # added a variable to store capitalized user input data
    countries.append(country_cap)
    # countries list now appends the capitalized input
    print(countries)
    # fixed indentation for the print function