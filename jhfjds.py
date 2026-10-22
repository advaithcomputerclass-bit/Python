expenses = []


# Function to add an expense
def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    expense = {
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(expense)

    print("Expense added successfully!")


# Function to view expenses
def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\n===== YOUR EXPENSES =====")

        for expense in expenses:
            print("Category:", expense["category"])
            print("Amount:", expense["amount"])
            print("Note:", expense["note"])
            print("------------------------")


# Function to calculate total
def calculate_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense:", total)


# Main program
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        calculate_total()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
