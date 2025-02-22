from rich import print
from .utils import read_expenses, write_expenses
from datetime import datetime


def add_expenses(description, amount):
    try:
        amount = float(amount)
        if amount <= 0:
            print("The amount must be [green bold]greater[/green bold] than 0")
            return False
    except ValueError as e:
        print(f"[red]Error: Invalid amount format - {e}[/red]")
        return False
            
    expenses = read_expenses()
    if expenses is None:
        expenses = []

    expense_id = 1 if len(expenses) == 0 else expenses[-1]["id"] + 1
    
    expenses.append ({
        "id": expense_id,
        "date": datetime.now().isoformat(),
        "description": description,
        "amount": amount,
    })
        
    write_expenses(expenses)
    print(f"Expense [bold green]added[/bold green] successfully (ID: {expense_id})")
        
