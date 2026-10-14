full_name = input("Enter your full name: ")
name_parts = full_name.split()
if len(name_parts) >= 2:
    first_name = name_parts[0]
    last_name = name_parts[-1]
    initials = first_name[0].upper() + ". " + last_name[0].upper() + "."
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Initials:", initials)
    print("Uppercase name:", full_name.upper())
    print("Reversed name:", full_name[::-1])
else:
    print("Please enter your first and last name.")