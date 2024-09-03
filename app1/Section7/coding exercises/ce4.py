# Use Python to create a file with name file.txt and write the text snail there.

file = open('file.txt', 'w')
# creates/opens file.txt
content = "snail"
# "snail" string is stored as a variable content
write_text = file.write(content)
# content is written into the file.txt using the write method