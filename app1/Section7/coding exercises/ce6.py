# Then, create a program that:
#
# 1. generates multiple text files by iterating over the filenames list,
#
# 2. and writes the text Hello inside each generated text file.

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
# for-loop to iterate the text in each files
    file = open(f'coding-exercises-files/{filename}', 'w')
    # opens the folder 'coding-exercises-files' in write mode
    file.write("Hello")
    # writes "Hello" into each filenames until all filenames have the content
    file.close()