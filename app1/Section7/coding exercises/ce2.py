# Take a look at the essay.txt file tab. That file contains some text.
#
# You should create a program that reads the essay.txt file,
# converts the first letter of each word to uppercase and prints out the converted text.

essay = open('essay.txt', 'r')
# open the essay.txt file
content = essay.read()
# read the text file
print(content.title())
# print the contents of text file using title method to capitalize the first letter of each word