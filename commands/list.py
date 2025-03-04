from .utils import read_expenses


def list_expenses():
    list_of_expenses = read_expenses()
    for i in list_of_expenses:
        print(i)
