password = input("Enter your password: ")
has_upper = False
has_lower = False
has_number = False
for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_number = True
if len(password) < 6:
    print("Weak password")
elif len(password) >= 8 and has_upper and has_lower and has_number:
    print("Strong password")
elif len(password) >= 6:
    print("Moderate password")
else:
    print("Weak password")