"""This module contains a list-printing function that
uses recursion to print each item in a list."""
def print_item(item):
    if (isinstance(item, list)):
        for i in item:
            print_item(i)
    else:
        print(item)
