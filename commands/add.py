from rich import print
from utils import read_expenses, write_expenses
from datetime import datetime


def add_expenses(amount, description):
    amount = float(amount)
    if amount <= 0:
        print("The amount must be [green bold] greater [/green bold] than 0")
        return
    try:
        if round(amount, 2) != amount:
            print("Enter the amount [red] correct amount [/red]")
            return
        print(
            f"Expense added: [green]{amount}[/green], Description: [cyan]{description}[/cyan]"
        )
    except ValueError as e:
        print(f"The error is,[red] {e} [/red]")

    expenses = read_expenses()

    if len(expenses) == 0:
        expenses_id = 1
    else:
        expenses_id = expenses_id[-1]["id"] + 1

    expenses.append(
        {
            "id": expenses_id,
            "date": datetime.now().isoformat(),
            "description": description,
            "amount": amount,
        }
    )

    write_expenses(expenses)
    print(f"Expense [bold green]added[/bold green] successfully (ID: {expense_id})")
