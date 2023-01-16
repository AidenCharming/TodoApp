date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"Journal/{date}.txt", "w") as file:
    file.write("Today's mood was " + mood + "\n")
    file.write("Thoughts about today are: " + thoughts)