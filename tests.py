import pytest
from expense import Expense, ExpenseTracker

def test_expense_creation():
    expense = Expense('2023-04-27', 'Food', 15.99, 'Lunch')
    assert expense.date == '2023-04-27'
    assert expense.category == 'Food'
    assert expense.amount == 15.99
    assert expense.description == 'Lunch'

def test_expense_tracker_add_and_view():
    expense_tracker = ExpenseTracker('test_expenses.csv')
    expense_tracker.add_expense('2023-04-27', 'Food', 15.99, 'Lunch')
    expenses = expense_tracker.expenses
    assert len(expenses) == 1
    assert expenses[0].date == '2023-04-27'
    assert expenses[0].category == 'Food'
    assert expenses[0].amount == 15.99
    assert expenses[0].description == 'Lunch'
