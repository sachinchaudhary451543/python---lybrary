import json
import os
from datetime import datetime

class BankSystem:
    def __init__(self):
        self.accounts_file = "accounts.json"
        self.accounts = self.load_accounts()

    # Load existing accounts from file
    def load_accounts(self):
        if os.path.exists(self.accounts_file):
            with open(self.accounts_file, "r") as file:
                return json.load(file)
        return {}

    # Save accounts to file
    def save_accounts(self):
        with open(self.accounts_file, "w") as file:
            json.dump(self.accounts, file, indent=4)

    # Register a new account
    def create_account(self):
        acc_no = input("\n📌 Enter a new 6-digit account number: ")
        if acc_no in self.accounts:
            print("❌ Account number already exists! Try logging in.")
            return None

        name = input("👤 Enter your full name As on PAN: ")
        while True:
            try:
                balance = int(input("💰 Enter initial deposit (Min ₹10,000): "))
                if balance < 10000:
                    print("❌ Minimum ₹10,000 required!")
                else:
                    break
            except ValueError:
                print("❌ Enter a valid amount!")

        self.accounts[acc_no] = {
            "name": name,
            "balance": balance,
            "transactions": []
        }
        self.save_accounts()
        print(f"✅ Account created successfully! Your Account Number: {acc_no}")
        return acc_no

    # Login existing user
    def login(self):
        acc_no = input("\n🔑 Enter your 6-digit account number: ")
        if acc_no in self.accounts:
            print(f"\n✅ Welcome back, {self.accounts[acc_no]['name']}!")
            self.view_account_details(acc_no)  # Show account details after login
            return acc_no
        else:
            print("❌ Account not found! Please create an account or recover your account.")
            return None

    # Forgot Account Number - Recover using Name
    def recover_account(self):
        name = input("\n🔍 Enter your full name (AS ON PAN )to recover your account: ")
        found = False
        for acc_no, details in self.accounts.items():
            if details["name"].lower() == name.lower():
                print(f"✅ Account Found! Your Account Number is: {acc_no}")
                found = True
                break
        if not found:
            print("❌ No account found with this name. Please check your details or create a new account.")

    # View Account Details
    def view_account_details(self, acc_no):
        print("\n📄 Account Details:")
        print(f"🔹 Account Number: {acc_no}")
        print(f"🔹 Account Holder: {self.accounts[acc_no]['name']}")
        print(f"🔹 Current Balance: ₹{self.accounts[acc_no]['balance']}")

    # Perform banking operations
    def operate_account(self, acc_no):
        while True:
            print("\n🔹Choose the  Option:")
            print("1️⃣ Check Balance")
            print("2️⃣ Debit Money")
            print("3️⃣ Credit Money")
            print("4️⃣ View Transaction History")
            print("5️⃣ Exit")

            choice = input("👉 Enter your choice: ")

            if choice == "1":
                print(f"💰 Current Balance: ₹{self.accounts[acc_no]['balance']}")
            elif choice == "2":
                self.debit(acc_no)
            elif choice == "3":
                self.credit(acc_no)
            elif choice == "4":
                self.view_transactions(acc_no)
            elif choice == "5":
                print("🚪 Exiting... Thank you for using our service! 🙌")
                self.save_accounts()
                break
            else:
                print("❌ Invalid choice! Please select a valid option.")

    # Get current date and time
    def get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Debit money from account
    def debit(self, acc_no):
        try:
            amount = int(input("💸 Enter amount to debit: "))
            if amount > self.accounts[acc_no]["balance"]:
                print("❌ Insufficient balance!")
            else:
                self.accounts[acc_no]["balance"] -= amount
                transaction = f"Debited ₹{amount} on {self.get_timestamp()}"
                self.accounts[acc_no]["transactions"].append(transaction)
                print(f"✅ ₹{amount} debited successfully.")
        except ValueError:
            print("❌ Enter a valid amount!")

    # Credit money to account
    def credit(self, acc_no):
        try:
            amount = int(input("💵 Enter amount to credit: "))
            self.accounts[acc_no]["balance"] += amount
            transaction = f"Credited ₹{amount} on {self.get_timestamp()}"
            self.accounts[acc_no]["transactions"].append(transaction)
            print(f"✅ ₹{amount} credited successfully.")
        except ValueError:
            print("❌ Enter a valid amount!")

    # View transaction history
    def view_transactions(self, acc_no):
        print("\n📜 Transaction History:")
        if self.accounts[acc_no]["transactions"]:
            for tx in self.accounts[acc_no]["transactions"]:
                print(f"🔹 {tx}")
        else:
            print("🔹 No transactions yet!")

# Main function
def main():
    system = BankSystem()
    print("\n🏦 Welcome to Secure Bank System!")

    while True:
        print("\n🔹 Main Menu:")
        print("1️⃣ Create Account")
        print("2️⃣ Login to Existing Account")
        print("3️⃣ Forgot Account Number")
        print("4️⃣ Exit")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            acc_no = system.create_account()
            if acc_no:
                system.operate_account(acc_no)
        elif choice == "2":
            acc_no = system.login()
            if acc_no:
                system.operate_account(acc_no)
        elif choice == "3":
            system.recover_account()
        elif choice == "4":
            print("🚪 Exiting... Thank you for banking with us! 🙌")
            break
        else:
            print("❌ Invalid choice! Please select a valid option.")

# Run the banking system
if __name__ == "__main__":
    main()
