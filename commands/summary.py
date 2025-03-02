from datetime import datetime
from .utils import read_expenses, get_month_text
from rich import print


def expenses_summary(month=None):
    expenses = read_expenses()
    if not expenses:
        print("[bold red]No expenses found.[/bold red]")
        return

    # Filter expenses by month if specified
    if month:
        filtered_expenses = [
            expense
            for expense in expenses
            if datetime.fromisoformat(expense["date"]).month == month
        ]
        if not filtered_expenses:
            print(f"[yellow]No expenses found for {get_month_text(month)}[/yellow]")
            return False

        month_text = f"for {get_month_text(month)}"
        total_amount = sum(expense["amount"] for expense in filtered_expenses)
    else:
        total_amount = sum(expense["amount"] for expense in expenses)
        month_text = ""

    formatted_total = f"Rs {total_amount:,.2f}"
    print(
        f"[green]The total amount{' ' + month_text if month_text else ''} is {formatted_total}[/green]"
    )
    return True
