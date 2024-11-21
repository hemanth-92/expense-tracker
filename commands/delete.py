from rich import print
from utils import read_expenses,write_expenses


def delete_expenses(expense_id):
    expenses = read_expenses()

    if not expenses:
        print("There is [red] no expenses [/red]")
    
    if not (expense['id'] == expense_id for expense in expenses):
        print("[red] There is no expenses with that id[/red]")

    expenses = [expense for expense in expenses if expense['id'] != expense_id]
    write_expenses(expenses)