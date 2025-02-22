from rich import print
from commands.add import add_expenses
from commands.list import list_expenses
from commands.delete import delete_expenses
from commands.summary import expenses_summary

import argparse

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
subparsers  = parser.add_subparsers(dest='command',help='Subcommands')

parser_add = subparsers.add_parser('add',help='Add new expenses')
parser_add.add_argument('--description',required=True,type=str,help="Add the Expense Description")
parser_add.add_argument('--amount',required=True,type=int,help="Add amount")

#parser for list
parser_list = subparsers.add_parser("list",help="List all the Expenses")

#parser for summary
parser_summary = subparsers.add_parser("summary",help="Summary of the all Expenses")
parser_summary.add_argument('--month',type=int,help="Add month (1-12) for the expenses")

#parser for delete
parser_delete = subparsers.add_parser("delete",help="delete the expenses")
parser_delete.add_argument('--id',type=int,required=True,help="Delete based on the id")

#parse the arguments
args = parser.parse_args()


match args.command:
  case 'add':
    add_expenses(args.description,args.amount)
  case 'list':
    list_expenses()
  case 'summary':
    expenses_summary(args.month)
  case 'delete':
    delete_expenses(args.id)
  case _:
    parser.print_help()
