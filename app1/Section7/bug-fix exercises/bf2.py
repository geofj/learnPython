# The code below tries to write the string "100.2" to the text file.
# However, there is an error. Try to fix the error.
#
# file = open("data.txt", 'r')
# file.write("100.12")
# file.close()

file = open("data2.txt", 'w')
# changed "r" to "w" so content can be written to the txt file
file.write("100.12")
file.close()