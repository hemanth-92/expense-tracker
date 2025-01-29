from rich import print
from commands.add import add_expenses
from commands.list import list_expenses
from commands.delete import delete_expenses


def command_Line(num):
    match num:
        case "1":
            print("[green] Show the list of expenses [/green]")
            list_expenses()
        case "2":
            print("Add the expenses")
            add_expenses(int, str)

        case "3":
            print("Delete the the expenses")
            delete_expenses(int)


print("Hello, [bold magenta]World[/bold magenta]!")
