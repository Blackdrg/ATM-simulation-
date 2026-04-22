import json
from datetime import datetime, date

DATA_FILE = "atm_data.json"
DAILY_LIMIT = 20000


def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


class ATM:
    def __init__(self, user_id, data):
        self.user_id = user_id
        self.data = data
        self.user = data[user_id]

    def display_balance(self):
        print(f"\nBalance: ₹{self.user['balance']}")

    def deposit(self, amount):
        if amount > 0:
            self.user['balance'] += amount
            self.record_transaction("Deposit", amount)
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        today = str(date.today())

        if today not in self.user['daily_withdraw']:
            self.user['daily_withdraw'][today] = 0

        if amount > self.user['balance']:
            print("Insufficient balance.")
        elif self.user['daily_withdraw'][today] + amount > DAILY_LIMIT:
            print("Daily withdrawal limit exceeded.")
        else:
            self.user['balance'] -= amount
            self.user['daily_withdraw'][today] += amount
            self.record_transaction("Withdraw", amount)
            print("Withdrawal successful.")

    def record_transaction(self, t_type, amount):
        entry = {
            "type": t_type,
            "amount": amount,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.user['transactions'].append(entry)

    def show_transactions(self):
        print("\nTransaction History:")
        for t in self.user['transactions']:
            print(f"{t['time']} - {t['type']} ₹{t['amount']}")


# User authentication
def authenticate(data):
    user_id = input("Enter User ID: ")
    pin = input("Enter PIN: ")

    if user_id in data and data[user_id]['pin'] == pin:
        print("Login successful.")
        return user_id
    else:
        print("Invalid credentials.")
        return None


def create_user(data):
    user_id = input("Create User ID: ")
    pin = input("Set PIN: ")

    if user_id in data:
        print("User already exists.")
        return

    data[user_id] = {
        "pin": pin,
        "balance": 0,
        "transactions": [],
        "daily_withdraw": {}
    }

    save_data(data)
    print("User created successfully.")


data = load_data()

while True:
    print("\n==== ATM SYSTEM ====")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == '1':
        user_id = authenticate(data)
        if user_id:
            atm = ATM(user_id, data)

            while True:
                print("\n===== ATM MENU =====")
                print("1. Display Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transactions")
                print("5. Logout")

                ch = input("Enter choice: ")

                if ch == '1':
                    atm.display_balance()

                elif ch == '2':
                    amt = float(input("Amount: "))
                    atm.deposit(amt)

                elif ch == '3':
                    amt = float(input("Amount: "))
                    atm.withdraw(amt)

                elif ch == '4':
                    atm.show_transactions()

                elif ch == '5':
                    save_data(data)
                    print("Logged out.")
                    break

                else:
                    print("Invalid option.")

    elif choice == '2':
        create_user(data)

    elif choice == '3':
        save_data(data)
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")