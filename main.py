from expense import Expense, ExpenseTracker

def main():
    expense_tracker = ExpenseTracker('expenses.csv')

    while True:
        print("Choose an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = int(input())

        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            description = input("Enter the description: ")

            expense_tracker.add_expense(date, category, amount, description)
            print("Expense added successfully!")
        elif choice == 2:
            print("Expenses:")
            expense_tracker.view_expenses()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
