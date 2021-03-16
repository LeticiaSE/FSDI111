import os

def print_menu():
    print("-----------------------------")
    print(" Warehouse management system ")
    print("-----------------------------")

    print('[1] Register new item')
    print('[2] Display catalog')
    print('[3] Items out of stock')
    print('[4] Detele item')
    print('[5] Update item stock')
    print('[6] Update item price')
    print('[7] print stock value')
    print('[8] print categories')

    print('[x] close')


def clear():
    #command = ''
    #if (os.name == 'nt'):
    #    command = 'cls'    
    #else:
    #    command 'clear'
    #return os.system(command)

    return os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    clear()
    print("-" * 80)
    print(title)
    print("-" * 80)

def print_item(item):
    print(
        str(item.id).rjust(3)
        + " | " + item.title.ljust(25)  #ljust sirve para dar espacios entre las columnas
        + " | " + item.category.ljust(12)
        + " | " + str(item.stock).rjust(11)
        + " | $" + str(item.price).rjust(14)

    )

"""def print_option(item):
    print("elija la opcion a eliminar por id")
"""

"""
travel the catalog
get the category of item
ask, if the category does not exist in x array
    push the category into x array
    print the category
"""