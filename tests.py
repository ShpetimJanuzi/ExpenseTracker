import pytest
from expense import Expense
from expense_tracker import ExpenseTracker

def test_expense_creation():
    expense = Expense('2023-04-27', 'Food', 15.99, 'Lunch')
    assert expense.date == '2023-04-27'
    assert expense.category == 'Food'
    assert expense.amount == 15.99
    assert expense.description == 'Lunch'

def test_expense_tracker_add_and_view():
    expense_tracker = ExpenseTracker('test_expensess.csv')
    initial_expenses_count = len(expense_tracker.expenses)
    expense_tracker.add_expense('2023-04-27', 'Food', 15.99, 'Lunch')
    expenses = expense_tracker.expenses
    assert len(expenses) == initial_expenses_count + 1
    assert expenses[-1].date == '2023-04-27'
    assert expenses[-1].category == 'Food'
    assert expenses[-1].amount == 15.99
    assert expenses[-1].description == 'Lunch'

