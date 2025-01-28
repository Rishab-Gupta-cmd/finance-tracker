from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

class Transaction:
    """One transaction."""
    def __init__(self, amount, category, description=""):
        self.amount = amount
        self.category = category.strip().capitalize() if category else "Miscellaneous"
        self.description = description
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.timestamp} | {self.category}: ${self.amount:.2f} - {self.description}"

class FinancialTracker:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, description=""):
        if amount <= 0:
            print("Income amount must be positive.")
            return
        self.transactions.append(Transaction(amount, "Income", description))

    def add_expense(self, amount, category="Miscellaneous", description=""):
        if amount <= 0:
            print("Expense amount must be positive.")
            return
        sanitized_category = category.strip().capitalize()
        self.transactions.append(Transaction(-amount, sanitized_category, description))

    def calculate_balance(self):
        return sum(transaction.amount for transaction in self.transactions)

    def view_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
            return
        print(f"Total Transactions: {len(self.transactions)}")
        for transaction in self.transactions:
            print(transaction)

    def view_summary(self):
        total_income = sum(t.amount for t in self.transactions if t.amount > 0)
        total_expenses = -sum(t.amount for t in self.transactions if t.amount < 0)
        balance = self.calculate_balance()

        print("--- Financial Summary ---")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}")

        # Enhanced Visualization: Pie Chart
        if total_income > 0 or total_expenses > 0:
            labels = ['Income', 'Expenses']
            sizes = [total_income, total_expenses]
            colors = ['lightgreen', 'lightcoral']

            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
            plt.title("Income vs Expenses")
            plt.show()
        else:
            print("No data available for visualization.")

    def clear_transactions(self):
        self.transactions = []
        print("All transaction history cleared successfully.")

    def view_spending_graph(self):
        expenses = defaultdict(float)
        for t in self.transactions:
            if t.amount < 0:
                expenses[t.category] += -t.amount

        if not expenses:
            print("No expenses to display.")
            return

        categories = list(expenses.keys())
        amounts = list(expenses.values())

        plt.bar(categories, amounts, color='skyblue')
        plt.xlabel("Categories")
        plt.ylabel("Total Spendings ($)")
        plt.title("Spending by Category")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty. Please try again.")

if __name__ == "__main__":
    tracker = FinancialTracker()

    while True:
        print(f"\n--- Personal Financial Tracker --- (Balance: ${tracker.calculate_balance():.2f})")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. View Summary")
        print("5. Clear Transaction History")
        print("6. Exit")
        print("7. View Spending Graph")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            description = input("Enter description (optional): ")
            tracker.add_income(amount, description)
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = get_non_empty_input("Enter expense category: ")
            description = input("Enter description (optional): ")
            tracker.add_expense(amount, category, description)
        elif choice == "3":
            tracker.view_transactions()
        elif choice == "4":
            tracker.view_summary()
        elif choice == "5":
            tracker.clear_transactions()
        elif choice == "6":
            confirm = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm == "y":
                print("Exiting tracker. Goodbye!")
                break
            else:
                print("Returning to the menu.")
        elif choice == "7":
            tracker.view_spending_graph()
        else:
            print("Invalid choice. Please try again.")
