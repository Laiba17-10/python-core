bank_balance = 5000
def deposit(amount):
    global bank_balance
    if amount > 0:
        bank_balance += amount
        print("Amount deposited:", amount)
    else:
        print("Invalid deposit amount.")
def withdraw(amount):
    global bank_balance
    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > bank_balance:
        print("Insufficient balance.")
    else:
        bank_balance -= amount
        print("Amount withdrawn:", amount)
deposit(1000)
print("Balance after deposit:", bank_balance)
withdraw(2000)
print("Balance after withdrawal:", bank_balance)