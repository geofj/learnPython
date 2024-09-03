contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slicing process was well presented." ]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
# zip method joins two or more objects into a single object, in this case, contents and filenames
    file = open(f"bonus-files/{filename}", 'w')
    # opens the files located within bonus-files in write mode
    file.write(content)
    # writes the list of content into the respective list of filenames