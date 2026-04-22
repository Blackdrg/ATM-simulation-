class ATM:
    def __init__(self):
        self.balance = 0
        self.transactions = []

  
    def display_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")

   
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ₹{amount}")
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

   
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")

    
    def show_transactions(self):
        print("\nTransaction History:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions:
                print("-", t)


atm = ATM()

while True:
    print("\n===== ATM MENU =====")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        atm.display_balance()

    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)

    elif choice == '4':
        atm.show_transactions()

    elif choice == '5':
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice. Please try again.")