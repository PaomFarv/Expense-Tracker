import csv

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
                
                if not (1 <= month <= 12 and 1 <= day <= 31 and year > 2025):
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

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to display.\n")
            return
        
        print("\n                    << Expenses >>\n")
        print(f"{'Date':<20}{'Description':<30}{'Amount ($)':<15}")
        for i in range(len(self.expenses)):
            print(f"{i + 1}. {self.date[i]:<20}{self.description[i]:<30}{self.expenses[i]:<15}")
        print("\n")

    def del__expense(self):
        if not self.expenses:
            print("No expenses to delete.\n")
            return
        
        self.view_expenses()
        
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
        print("Expense deleted successfully.\n")

    def total_expenses(self):
        if not self.expenses:
            print("No expenses to calculate total.\n")
            return
        
        total = sum(self.expenses)
        print(f"Total expenses: ${total:.2f}\n")

app = Expense()

def menu():
        print()
        print("^" * 100)
        print("\nWelcome to the Expense Tracker !")
        print("Please choose an option:\n")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Remove an expense")
        print("4. Total expenses")
        print("5. Exit\n")
        print("^" * 100)

while True:
    menu()
    choice = input("Please enter your choice (1-5): ")
    
    if choice == "1":
        app.add_expense()

    elif choice == "2":
        app.view_expenses()

    elif choice == "3":
        app.del__expense()
    
    elif choice == "4":
        app.total_expenses()
    
    elif choice == "5":
        print("Exiting the program. Goodbye!\n")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")