bill = float(input("Enter total bill amount: "))
tip_percentage = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))
if bill >= 0 and tip_percentage >= 0 and people > 0:
    tip = bill * tip_percentage / 100
    total_bill = bill + tip
    per_person = total_bill / people

    print("Total tip:", tip)
    print("Total bill including tip:", total_bill)
    print("Each person has to pay:", per_person)
else:
    print("Please enter valid amounts and number of people.")