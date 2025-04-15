class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # Debit method
    def debit(self, amount):
        if amount > self.balance:
            print("\n❌ Error: Insufficient balance! You do not have enough funds.")
        else:
            self.balance -= amount
            print(f"\n✅ Rs. {amount} was debited successfully.")
        self.show_options()  # Show options after transaction

    # Credit method
    def credit(self, amount):
        self.balance += amount
        print(f"\n✅ Rs. {amount} was credited successfully.")
        self.show_options()  # Show options after transaction

    # Method to get balance
    def get_balance(self):
        return self.balance

    # Show transaction options
    def show_options(self):
        while True:
            print("\n🔹Choose The Option:")
            print("1️⃣ Check Balance")
            print("2️⃣ Debit Money")
            print("3️⃣ Credit Money")
            print("4️⃣ Exit")

            choice = input("👉 Enter your choice: ")

            if choice == "1":
                print("💰 Your current balance is Rs.", self.get_balance())
            elif choice == "2":
                amount = int(input("💸 Enter the amount to debit: "))
                self.debit(amount)
                break  # Ensure options reappear after transaction
            elif choice == "3":
                amount = int(input("💵 Enter the amount to credit: "))
                self.credit(amount)
                break  # Ensure options reappear after transaction
            elif choice == "4":
                print("🚪 Exiting... Thank you for using our service! 🙌")
                exit()
            else:
                print("❌ Invalid choice! Please select a valid option.")

# Create account instance
acc1 = Account(10000, 451543)
print("\n👋 Welcome to Your Bank Account!")
print("🏦 Your account number is:", acc1.account_no)

# Start transaction options
acc1.show_options()
