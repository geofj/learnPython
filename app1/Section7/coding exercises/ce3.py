# Write a program that reads the essay.txt file and
# returns the number of characters contained in the file.

essay = open('essay.txt', 'r')
# opens essay.txt file
content = essay.read()
# reads the content of essay.txt
characters = len(content)
# len function calculated the number of characters in content variable
print(f"The file contains {characters} characters.")
# prints the number of characters in essay.txt