newmember = input("Please enter the name of the new member: ")

file = open("Files/members.txt", "r")
members = file.readlines()
file.close()

members.append(newmember + "\n")

file = open("Files/members.txt", "w")
file.writelines(members)
file.close()
