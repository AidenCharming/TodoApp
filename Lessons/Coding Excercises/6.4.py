filenames = ["Hola.txt", "Bonjour.txt", "Konichiwa.txt"]

for filename in filenames:
    file = open(f"Files/{filename}", "w")
    file.write("Hello")
    file.close()