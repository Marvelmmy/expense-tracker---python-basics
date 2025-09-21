# Expense Tracker (Class-based)
from datetime import datetime, timedelta
import csv
import os

class ExpenseTracker:
    def __init__(self, csv_file="expenses.csv"):
        self.expenses = []
        self.csv_file = csv_file
        self.keys = ["item", "amount", "category", "due date"]

    def menu(self):
        while True:
            os.system("clear")  # For Linux/Mac. Use "cls" for Windows
            print("\n=== EXPENSE TRACKER ===")
            print("1. View Expenses")
            print("2. Add Expense")
            print("3. Save to CSV")
            print("4. Load from CSV")
            print("5. Monthly Summary")
            print("6. Exit")

            try:
                choice = int(input("Choose (1-6): "))
                if choice == 1:
                    self.view_expenses()
                elif choice == 2:
                    self.add_expense()
                elif choice == 3:
                    self.save_to_csv()
                elif choice == 4:
                    self.load_from_csv()
                elif choice == 5:
                    self.monthly_summary()
                elif choice == 6:
                    print("Exiting expense tracker...")
                    break
                else:
                    print("Invalid option. Try again.")
                input("\nPress Enter to continue...")
            except ValueError:
                print("Please enter a number (1-6).")
                input("\nPress Enter to continue...")

    def view_expenses(self):
        if self.expenses:
            print("\n--- Your Expenses ---")
            for exp in self.expenses:
                print(f"- {exp['item']}: ${exp['amount']} "
                      f"({exp['category']}, due {exp['due date']})")
        else:
            print("No expenses recorded yet.")

    def add_expense(self):
        try:
            item = input("Item: ")
            amount = float(input("Amount: $"))
            category = input("Category: ")
            due_days = int(input("Due in how many days?: "))

            due_date = datetime.today() + timedelta(days=due_days)

            expense = {
                "item": item,
                "amount": amount,
                "category": category,
                "due date": due_date.strftime("%Y-%m-%d")
            }

            self.expenses.append(expense)
            print("\n✅ Expense added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def save_to_csv(self):
        try:
            with open(self.csv_file, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.keys)
                writer.writeheader()
                writer.writerows(self.expenses)
            print(f"✅ Expenses saved to {self.csv_file}")
        except Exception as e:
            print(f"Error saving to CSV: {e}")

    def load_from_csv(self):
        try:
            with open(self.csv_file, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                self.expenses.clear()
                for row in reader:
                    row["amount"] = float(row["amount"])
                    self.expenses.append(row)
            print(f"✅ Expenses loaded from {self.csv_file}")
        except FileNotFoundError:
            print(f"Error: {self.csv_file} not found.")
        except Exception as e:
            print(f"Error loading from CSV: {e}")

    def monthly_summary(self):
        if not self.expenses:
            print("No expenses to summarize.")
            return

        total = 0
        today = datetime.today()
        print("\n--- Monthly Summary ---")
        for exp in self.expenses:
            try:
                due_date = datetime.strptime(exp["due date"], "%Y-%m-%d")
                if due_date.month == today.month and due_date.year == today.year:
                    total += exp["amount"]
            except Exception:
                print(f"⚠️ Skipping invalid expense: {exp}")
        print(f"Total for {today.strftime('%B %Y')}: ${total:.2f}")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.menu()
