# In the coding area, we have defined a country variable "India".
#
# You should write a match-case block that checks the value of the country variable and:
#
# Prints out Hello if the value of country is "USA".
#
# Prints out Namaste if the value of country is "India".
#
# Prints out Hallo if the value of country is "Germany".

country = "India"
# country variable with "India" as the string

match country:
    case 'Germany':
        print("Hallo")
    case 'India':
        print("Namaste")
    # since "India" is our given variable, this case will trigger and print "Namaste"
    case 'USA':
        print("Hello")
    # match case function will check the variable and match it the defined cases
