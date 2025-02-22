from rich import print
from .utils import read_expenses, write_expenses


def delete_expenses(expense_id):
    expenses = read_expenses()

    if not expenses:
        print("[red]No expenses found[/red]")
        return

    if not any(expense["id"] == expense_id for expense in expenses):
        print(f"[red]No expense found with ID: {expense_id}[/red]")
        return

    expenses = [expense for expense in expenses if expense["id"] != expense_id]
    write_expenses(expenses)
    print(f"[green]Successfully deleted expense with ID: {expense_id}[/green]")
