import csv
import os
from expense import Expense

class ExpenseTracker:
    def __init__(self, filename):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    expense = Expense(row['date'], row['category'], row['amount'], row['description'])
                    self.expenses.append(expense)

    def save_expenses(self):
        with open(self.filename, 'w') as csvfile:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow({'date': expense.date, 'category': expense.category, 'amount': expense.amount, 'description': expense.description})

    def add_expense(self, date, category, amount, description):
        expense = Expense(date, category, amount, description)
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        for expense in self.expenses:
            print(f"{expense.date}, {expense.category}, {expense.amount}, {expense.description}")
