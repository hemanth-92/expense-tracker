from rich import print
from .utils import read_expenses, write_expenses

def delete_expenses(expense_id):
    expenses = read_expenses()
    
    try:
        expense_id = int(expense_id) if not isinstance(expense_id, int) else expense_id
    except (ValueError, TypeError):
        pass
        
    if not expenses:
        print("[red]No expenses found[/red]")
        return False
        
    if not any(str(expense["id"]) == str(expense_id) for expense in expenses):
        print(f"[red]No expense found with ID: {expense_id}[/red]")
        return False
        
    expenses = [expense for expense in expenses if str(expense["id"]) != str(expense_id)]
    write_expenses(expenses)
    print(f"[green]Successfully deleted expense with ID: {expense_id}[/green]")
    return True