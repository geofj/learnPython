filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
# for-loop to reassign names for each string in filenames list
    filename = filename.replace('.', '-', 1)
    # replace function replaces previous data with the new args provided, into a new variable
    # (old, new, character to replace (0, 1, 2 etc))
    print(filename)
    # print the newly modified filenames