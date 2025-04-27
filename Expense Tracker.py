import csv
import os
from colorama import Fore

class Expense:
    def __init__(self):
        self.expenses = []
        self.date = []
        self.description = []

    def add_expense(self):
        date = input("Enter the date (YYYY-MM-DD): ")  
        
        while True:
            try:
                date_parts = date.split("-")
                if len(date_parts) != 3:
                    raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
                
                year, month, day = map(int, date_parts)
                
                if not (1 <= month <= 12 and 1 <= day <= 31 and year >= 2025):
                    raise ValueError("Invalid date. Year should be from 2025 and Month should be between 1-12 and day should be between 1-31.")
                break

            except ValueError as e:
                print(e)
                date = input("Enter the date (YYYY-MM-DD): ")
        
        description = input("Enter the description: ")
        expense = input("Enter the expense amount: $")

        while True:
            try:
                expense = float(expense)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for the expense amount.")
                expense = input("Enter the expense amount: $")
        
        print(f"Expense added Successfully.\n")
        
        self.expenses.append(expense)
        self.date.append(date)
        self.description.append(description)

        with open('expenses.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, description, expense])

    def view_expenses(self):
        file_path = "expenses.csv"
        if not os.path.exists(file_path):
            print("No prior expenses to display.\n")
            return
        
        self.date.clear()
        self.description.clear()
        self.expenses.clear()

        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            print("\n                    << Expenses >>\n")
            print(f"{'Date':<20}{'Description':<30}{'Amount ($)':<15}")
            i = 0
            for row in reader:
                date, description, expense = row
                self.date.append(date)
                self.description.append(description)
                self.expenses.append(float(expense))
                
                print(f"{i + 1}. {self.date[i]:<20}{self.description[i]:<30}{self.expenses[i]:<15}")
                i += 1
            print("\n")

    def del__expense(self):
        file_path = "expenses.csv"
        if not os.path.exists(file_path):
            print("No prior expenses to delete.\n")
            return

        self.date.clear()
        self.description.clear()
        self.expenses.clear()
        
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            print("\n                    << Expenses >>\n")
            print(f"{'Date':<20}{'Description':<30}{'Amount ($)':<15}")
            for i, row in enumerate(reader):
                date, description, expense = row
                self.date.append(date)
                self.description.append(description)
                self.expenses.append(float(expense))
                print(f"{i + 1}. {date:<20}{description:<30}{expense:<15}")
            print("\n")

        if not self.expenses:
            print("No prior expenses to delete.\n")
            return

        while True:
            try:
                index = int(input("Enter the index of the expense to delete: ")) - 1
                if index < 0 or index >= len(self.expenses):
                    raise IndexError("Invalid index. Please enter a valid index.")
                break
            except (ValueError, IndexError) as e:
                print(e)
        
        del self.expenses[index]
        del self.date[index]
        del self.description[index]

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for i in range(len(self.expenses)):
                writer.writerow([self.date[i], self.description[i], self.expenses[i]])

        print("Expense deleted successfully.\n")

    def total_expenses(self):
        file_path = "expenses.csv"
        if not os.path.exists(file_path):
            print("No prior expenses to calculate total.\n")
            return
        
        self.expenses.clear()

        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                expense = float(row[2])
                self.expenses.append(expense)
   
        total = sum(self.expenses)
        print(f"Total expenses: ${total:.2f}\n")

    def clear_all(self):
        file_path = "expenses.csv"
        if os.path.exists(file_path):
            os.remove(file_path)
        self.expenses.clear()
        self.date.clear()
        self.description.clear()

app = Expense()

def menu():
    print()
    print("^" * 100)
    print(Fore.GREEN + "\nWelcome to the Expense Tracker!")
    print("Please choose an option:\n")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Remove an expense")
    print("4. Total expenses")
    print("5. Clear all expenses")
    print("6. Exit")
    print("^" * 100)

while True:
    menu()
    choice = input("Please enter your choice (1-6): ")
    
    if choice == "1":
        app.add_expense()

    elif choice == "2":
        app.view_expenses()

    elif choice == "3":
        app.del__expense()
    
    elif choice == "4":
        app.total_expenses()
    
    elif choice == "5":
        app.clear_all()
        print("All expenses cleared successfully.\n")

    elif choice == "6":
        print("Exiting the program. Goodbye!\n")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")
