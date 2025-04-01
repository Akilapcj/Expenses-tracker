import json
import os

# File to store the expenses
EXPENSE_FILE = "expenses.json"

# Function to load existing expenses from a file
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    return {"income": [], "expenses": []}

# Function to save expenses to a file
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Function to add income
def add_income(expenses, amount, source):
    expenses["income"].append({"amount": amount, "source": source})
    print(f"Income of {amount} from {source} added.")

# Function to add an expense
def add_expense(expenses, amount, category, description):
    expenses["expenses"].append({"amount": amount, "category": category, "description": description})
    print(f"Expense of {amount} in category {category} added.")

# Function to show summary
def show_summary(expenses):
    total_income = sum(item["amount"] for item in expenses["income"])
    total_expenses = sum(item["amount"] for item in expenses["expenses"])
    balance = total_income - total_expenses

    print("\n---- Expense Summary ----")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

# Main function for the Expense Tracker app
def main():
    print("Welcome to the Expense Tracker!")

    # Load existing expenses data from the file
    expenses = load_expenses()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            amount = float(input("Enter income amount: $"))
            source = input("Enter income source: ")
            add_income(expenses, amount, source)
        elif choice == "2":
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category (e.g., Food, Rent): ")
            description = input("Enter a short description: ")
            add_expense(expenses, amount, category, description)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            # Save expenses to file before exiting
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
