password = input("Enter your password: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["number"] = digit

uppercase = False
for u in password:
    if u.isupper():
        uppercase = True

result["Uppercase"] = uppercase

print(result)
if all(result.values()):
    print("Strong Password.")
else:
    print("Weak Password.")
