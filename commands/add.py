from rich import print

def add_expenses(amount,description):
    if amount <= 0:
        print("The amount must be [green bold] greater [/green bold] than 0")
