from datetime import datetime
from utils import read_expenses, get_month_text


def summary(month=None):
    expenses = read_expenses()
    if not expenses:
        print("[bold red]No expenses found.[/bold red]")
        return

    month = ""

    if month:
        expenses = [
            expenses
            for expense in expenses
            if datetime.fromisoformat(expense["date"]).month == month
        ]
        month_text = f"for {get_month_text}"

    total_amount = sum(expenses["amount"] for expense in expenses)

    print(f"The totat amount is {total_amount}")

