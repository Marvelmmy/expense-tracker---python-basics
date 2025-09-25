# Personalized Finance Manager

import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os
import time

class FinanceManager:
    def __init__(self, csv_file):
        self.transactions = [] 
        self.keys = ["type", "item", "amount", "category", "date"]
        self.csv_file = csv_file

    def main_menu(self):
        os.system("clear")
        while True:
            print("\n--------------- MAIN MENU ---------------")
            print("1. Add transaction (income/expense)")
            print("2. View current balance")
            print("3. View transactions")
            print("4. Generate category breakdown (expenses)")
            print("5. Save transactions to CSV")
            print("6. Load transactions from CSV")
            print("7. Exit")

            try:
                choice = int(input("Choose (1-8): "))
                if choice == 1:
                    self.add_transaction()
                elif choice == 2:
                    self.view_current_balance()
                elif choice == 3:
                  self.view_transaction()
                elif choice == 4:
                    self.generate_category_breakdown()
                elif choice == 5:
                    self.save_to_csv()
                elif choice == 6:
                    self.load_from_csv()
                elif choice == 7:
                    print("Exiting finance manager...")
                    break
                else:
                    print("Invalid option. Try again.")
           
            except ValueError:
                print("Please enter a number (1-8).")
            except KeyboardInterrupt:
                print("Okay, goodbye!")
                break

            time.sleep(0.5)

    def add_transaction(self):
        os.system('clear')
        try:
          choice = input("Add your transaction (income/expense): ").lower()
          if choice not in ['income', 'expense']:
              print("Invalid transaction type. Please enter 'income' or 'expense'.")
              return

          item = input("item: (ex: Salary / Others / Bills)")
          amount = float(input("amount: "))
          category = input("category: (ex. bills, food, personal, fun)")
          date_str = input("Enter date (YYYY-MM-DD): ")
          date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")

          due_date = ""
          if choice == 'expense':
            due_days = int(input("due in how many days: "))
            due_date = (datetime.now() + timedelta(days=due_days)).strftime("%Y-%m-%d")

          # define each element for each transaction 
          transaction = {
              'type': choice,
              'item' : item,
              'amount': amount,
              'category': category,
              'date': date,
              'due date': due_date
          }

          self.transactions.append(transaction)
          print("\n✅ Added transaction:", transaction, "\n")

        except ValueError as e:
          print(f"Invalid input: {e}")

        except KeyboardInterrupt:
          print("Okay, goodbye!")

        time.sleep(0.5)


    def view_current_balance(self):
      os.system('clear')
      if self.transactions:
        try:
          df = pd.DataFrame(self.transactions)

          income = df[df['type'] == 'income']['amount'].sum() # the total amount of incomes
          expense = df[df['type'] == 'expense']['amount'].sum() # the total amount of expenses


          print(f"---- Your total income is $ {income:.2f} ----")
          print(f"---- Your total expenses is $ {expense:.2f} ----")
          print("___________________________________________________ -")
          print(f"---- Your balance is $ {income - expense:.2f} ----")

        except Exception as e:
          print(f"Error: {e}")

        except KeyboardInterrupt:
          print("Okay, goodbye!")
      else:
        print("No transactions found!")
      time.sleep(0.5)

    def view_transaction(self):
      os.system('clear')
      if self.transactions:
        try:
          print("------ All Transactions ------")
          for idx, transaction in enumerate(self.transactions, start=1): # to iterate key and values from each dictionary in transactions list 
            due_date_info = f" | Due Date: {transaction['due date']}" if transaction.get('due date') else "" # Checks if the transaction dictionary has a "due date" key.
            print(
                f"{idx}. {transaction['type'].capitalize()} | "
                f"Item: {transaction['item']} | "
                f"Amount: ${transaction['amount']:.2f} | "
                f"Category: {transaction['category']} | "
                f"Date: {transaction['date']}{due_date_info}"
            )
        except Exception as e:
              print(f"Error: {e}")

        except KeyboardInterrupt:
              print("Okay, goodbye!")
      else:
        print("No transactions found!")

      time.sleep(0.5)

    def generate_category_breakdown(self):
      os.system('clear')
      if self.transactions:
        try:
            df = pd.DataFrame(self.transactions)

            # expense category
            expense_df = df[df['type'] == 'expense']
            if not expense_df.empty:
              expense_slices = expense_df.groupby('category')['amount'].sum() 
              expense_labels = expense_slices.index

              # the pie chart
              plt.figure(figsize=(8, 8))
              plt.pie(expense_slices, labels=expense_labels, autopct='%1.1f%%', startangle=140) # to show the pie chart
              plt.title("Expense breakdown by Category")
              plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
              plt.show()
            else:
                print("No expense transactions found to generate a breakdown.")

        except Exception as e:
            print(f"Error: {e}")

        except KeyboardInterrupt:
            print("Okay, goodbye!")
      else:
        print("No transactions found!")
      time.sleep(0.5)

    def save_to_csv(self):
      os.system('clear')
      if self.transactions:
        try:
          with open(self.csv_file, 'w', newline='') as new_file: # write to blank csv file 
            fields = self.keys + ['due date']
            csv_writer = csv.DictWriter(new_file, fieldnames=fields) 
            csv_writer.writeheader()
            csv_writer.writerows(self.transactions)
          print(f"Transactions successfully saved to {self.csv_file}")

        except Exception as e:
          print(f"Error saving to CSV: {e}")

        except KeyboardInterrupt:
          print("Okay, goodbye!")
      else:
        print("No transactions to save to CSV!")

      time.sleep(0.5)

    def load_from_csv(self):
      os.system('clear')
      try:
          with open(self.csv_file, 'r') as csvfile: # read from csv file 
              reader = csv.DictReader(csvfile)
              self.transactions = []  # Clear existing transactions
              for row in reader:
                  # Convert amount to float
                  row['amount'] = float(row['amount'])
                  self.transactions.append(row)
          print(f"Successfully loaded expenses from {self.csv_file}")

      except FileNotFoundError:
          print(f"Error: {self.csv_file} not found.")
      except Exception as e:
          print(f"Error loading from CSV: {e}")
      except KeyboardInterrupt:
          print("Okay, goodbye!")


      time.sleep(0.5)


finance = FinanceManager('transactions.csv')
if __name__ == "__main__":
    finance.main_menu()
