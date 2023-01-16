filenames = ["a.txt", "b.txt""", "c.txt"]

for filename in filenames:
    file = open(f"Files/{filename}")
    read = file.read()
    print(read)