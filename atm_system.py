# ATM Management System

balance = 1000.0

def check_balance():
    print(f"\nYour current balance is: ₹{balance:.2f}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully!")
        print(f"New Balance: ₹{balance:.2f}")
    else:
        print("Please enter a valid amount.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully!")
        print(f"Remaining Balance: ₹{balance:.2f}")

def exit_atm():
    print("\nThank you for using our ATM.")
    print("Have a nice day!")

while True:
    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        exit_atm()
        break
    else:
        print("Invalid choice! Please select between 1 and 4.")