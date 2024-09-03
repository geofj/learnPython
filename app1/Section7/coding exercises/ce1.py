# On the side panel there's a bear.txt file. The existing code opens that file in read mode.
#
# Below that code, please read the file content and print out the content.

file = open("bear.txt")
# opens bear.txt file
read = file.read()
# read method reads the bear.txt file
file.close()
# closes file
print(read)
# prints the bear.txt file