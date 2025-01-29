from datetime import datetime
from utils import read_expenses, get_month_text
from rich import print


def summary(month=None):
    # Read expenses and handle empty case
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
            return

        month_text = f"for {get_month_text(month)}"
        total_amount = sum(expense["amount"] for expense in filtered_expenses)
    else:
        total_amount = sum(expense["amount"] for expense in expenses)
        month_text = ""

    # Format and print the total with currency
    formatted_total = f"${total_amount:,.2f}"
    print(
        f"[green]The total amount{' ' + month_text if month_text else ''} is {formatted_total}[/green]"
    )
