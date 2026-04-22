import json
from datetime import datetime, date
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

DATA_FILE = "atm_data.json"
DAILY_LIMIT = 20000


def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def safe_input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")


def safe_input_pin(prompt):
    while True:
        pin = input(prompt)
        if len(pin) == 4 and pin.isdigit():
            return pin
        print(f"{Fore.RED}PIN must be 4 digits.{Style.RESET_ALL}")


class ATM:
    def __init__(self, user_id, data):
        self.user_id = user_id
        self.data = data
        self.user = data[user_id]

    def display_balance(self):
        print(f"{Fore.GREEN}\nBalance: ₹{self.user['balance']}{Style.RESET_ALL}")

    def deposit(self, amount):
        if amount > 0:
            self.user['balance'] += amount
            self.record_transaction("Deposit", amount)
            print(f"{Fore.GREEN}Deposit successful.{Style.RESET_ALL}")
            self.display_balance()
        else:
            print(f"{Fore.RED}Invalid amount.{Style.RESET_ALL}")

    def withdraw(self, amount):
        today = str(date.today())

        if today not in self.user['daily_withdraw']:
            self.user['daily_withdraw'][today] = 0

        if amount > self.user['balance']:
            print(f"{Fore.RED}Insufficient balance.{Style.RESET_ALL}")
        elif self.user['daily_withdraw'][today] + amount > DAILY_LIMIT:
            print(f"{Fore.RED}Daily withdrawal limit (₹{DAILY_LIMIT}) exceeded.{Style.RESET_ALL}")
        elif amount <= 0:
            print(f"{Fore.RED}Invalid amount.{Style.RESET_ALL}")
        else:
            self.user['balance'] -= amount
            self.user['daily_withdraw'][today] += amount
            self.record_transaction("Withdraw", amount)
            print(f"{Fore.GREEN}Withdrawal successful.{Style.RESET_ALL}")
            self.display_balance()

    def record_transaction(self, t_type, amount):
        entry = {
            "type": t_type,
            "amount": amount,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.user['transactions'].append(entry)

    def show_transactions(self):
        print(f"{Fore.CYAN}\n=== Transaction History ==={Style.RESET_ALL}")
        if not self.user['transactions']:
            print(f"{Fore.YELLOW}No transactions yet.{Style.RESET_ALL}")
        else:
            for t in self.user['transactions']:
                print(f"{Fore.WHITE}{t['time']} - {t['type']}: ₹{t['amount']}{Style.RESET_ALL}")

    def change_pin(self, new_pin):
        self.user['pin'] = new_pin
        print(f"{Fore.GREEN}PIN changed successfully.{Style.RESET_ALL}")

    def transfer(self, target_id, amount):
        if target_id not in self.data:
            print(f"{Fore.RED}Target user not found.{Style.RESET_ALL}")
            return
        if amount > self.user['balance']:
            print(f"{Fore.RED}Insufficient balance.{Style.RESET_ALL}")
            return
        if amount <= 0:
            print(f"{Fore.RED}Invalid amount.{Style.RESET_ALL}")
            return
        self.user['balance'] -= amount
        self.data[target_id]['balance'] += amount
        self.record_transaction("Transfer Out", amount)
        self.data[target_id]['transactions'].append({
            "type": "Transfer In",
            "amount": amount,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"{Fore.GREEN}₹{amount} transferred to {target_id}.{Style.RESET_ALL}")


def authenticate(data):
    print(f"{Fore.CYAN}\n=== LOGIN ==={Style.RESET_ALL}")
    user_id = input(f"{Fore.CYAN}User ID: {Style.RESET_ALL}")
    pin = safe_input_pin(f"{Fore.CYAN}PIN: {Style.RESET_ALL}")

    if user_id in data and data[user_id]['pin'] == pin:
        print(f"{Fore.GREEN}Login successful! Welcome, {user_id}.{Style.RESET_ALL}")
        return user_id
    else:
        print(f"{Fore.RED}Invalid credentials.{Style.RESET_ALL}")
        return None


def create_user(data):
    print(f"{Fore.CYAN}\n=== CREATE ACCOUNT ==={Style.RESET_ALL}")
    user_id = input("User ID: ")
    pin = safe_input_pin("Set 4-digit PIN: ")

    if user_id in data:
        print(f"{Fore.RED}User already exists.{Style.RESET_ALL}")
        return

    data[user_id] = {
        "pin": pin,
        "balance": 0,
        "transactions": [],
        "daily_withdraw": {}
    }
    save_data(data)
    print(f"{Fore.GREEN}Account created for {user_id}.{Style.RESET_ALL}")


data = load_data()

print(f"{Fore.YELLOW}🚀 Advanced ATM Prototype{Style.RESET_ALL}")

while True:
    print(f"\n{Fore.MAGENTA}=== MAIN MENU ==={Style.RESET_ALL}")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit")

    choice = input(f"{Fore.CYAN}Choose option: {Style.RESET_ALL}")

    if choice == '1':
        user_id = authenticate(data)
        if user_id:
            atm = ATM(user_id, data)
            while True:
                print(f"\n{Fore.BLUE}===== {user_id.upper()} MENU ====={Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Balance: ₹{atm.user['balance']}{Style.RESET_ALL}")
                print("1. View Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transactions")
                print("5. Change PIN")
                print("6. Transfer")
                print("7. Logout")

                ch = input(f"{Fore.CYAN}Choice: {Style.RESET_ALL}")

                if ch == '1':
                    atm.display_balance()
                elif ch == '2':
                    amount = safe_input_number("Deposit amount: ₹")
                    atm.deposit(amount)
                elif ch == '3':
                    amount = safe_input_number("Withdraw amount: ₹")
                    atm.withdraw(amount)
                elif ch == '4':
                    atm.show_transactions()
                elif ch == '5':
                    new_pin = safe_input_pin("New PIN: ")
                    atm.change_pin(new_pin)
                    save_data(data)
                elif ch == '6':
                    target_id = input("Target User ID: ")
                    amount = safe_input_number("Transfer amount: ₹")
                    atm.transfer(target_id, amount)
                    save_data(data)
                elif ch == '7':
                    save_data(data)
                    print(f"{Fore.YELLOW}Logged out safely.{Style.RESET_ALL}")
                    break
                else:
                    print(f"{Fore.RED}Invalid option.{Style.RESET_ALL}")

    elif choice == '2':
        create_user(data)
    elif choice == '3':
        save_data(data)
        print(f"{Fore.YELLOW}Thank you for using ATM! 👋{Style.RESET_ALL}")
        break
    else:
        print(f"{Fore.RED}Invalid choice.{Style.RESET_ALL}")
