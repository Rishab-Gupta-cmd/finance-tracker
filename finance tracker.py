class Transaction:
    """one transaction."""
    def __init__(self, amount, category, description=""):
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.category}: ${self.amount:.2f} - {self.description}"


class FinancialTracker:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, description=""):
        if amount <= 0:
            print("Income amount must be positive.")
            return
        self.transactions.append(Transaction(amount, "Income", description))

    def add_expense(self, amount, category, description=""):
        if amount <= 0:
            print("Expense amount must be positive.")
            return
        self.transactions.append(Transaction(-amount, category, description))

    def get_balance(self):
        return sum(transaction.amount for transaction in self.transactions)

    def view_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
            return
        for transaction in self.transactions:
            print(transaction)

    def view_summary(self):
        total_income = sum(t.amount for t in self.transactions if t.amount > 0)
        total_expenses = -sum(t.amount for t in self.transactions if t.amount < 0)
        balance = self.get_balance()

        print("--- Financial Summary ---")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}")

    def clear_transactions(self):
        self.transactions = []
        print("All transaction history cleared successfully.")


if __name__ == "__main__":
    tracker = FinancialTracker()

    while True:
        print("\n--- Personal Financial Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Clear Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            description = input("Enter description (optional): ")
            tracker.add_income(amount, description)
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter description (optional): ")
            tracker.add_expense(amount, category, description)
        elif choice == "3":
            tracker.view_transactions()
        elif choice == "4":
            tracker.view_summary()
        elif choice == "5":
            tracker.clear_transactions()
        elif choice == "6":
            print("Exiting tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
