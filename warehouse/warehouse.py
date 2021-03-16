"""

-stock (int)
-price (float)

"""


# imports
from menu import print_menu, clear, print_header, print_item
from item import Item
import pickle

# global variables
catalog = []
last_id = 1
total = 0

# functions
def serialize_catalog():
    write = open('warehouse.data', 'wb') #open/create a file to write binary
    pickle.dump(catalog,write)
    write.close() # close the stream, release the file
    print("** Data serialized **")

def deserialize_catalog():
    global last_id
    try:
        reader = open('warehouse.data','rb') #open the file to read binary
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        how_many = len(catalog)
        last_item = catalog[-1]
        last_id = last_item.id + 1
        print("** Deserialized " + str(how_many) + " items **")
    except:
        print("** Error, not data found **")

def register_item():
    global last_id
    try:
        print_header("Register a new Item")
        title = input('please provide the Title: ')
        cat = input('please provide the Category: ')
        stock = int(input('please provide initial Stock: '))
        price = float(input('please provide the Price: '))

        item = Item(last_id, title, cat, stock, price)
        last_id = last_id + 1
        catalog.append(item)

        print(" ** Item Saved! **")
    
    except ValueError:
        print('** Error, incorrect input fix and try again **')

    except:
        print('** Error, something went wrong **')

def print_catalog():
    print_header("Items on Catalog")

    if( len(catalog) == 0):
        print("** Your catalog is empty ** \nUse option 1 to create items\n")
    else:
        for item in catalog:
            print_item(item)
        
        print("-" * 80)

def print_stock_empty():
    print_header("empty")
    for item in catalog:
        if(item.stock == 0):
            print(item.title) 

def print_value_total():
    print_header("empty")
    sum = 0
    for item in catalog:
        total = (item.stock * item.price)
        sum = sum + total
    print(sum)

def delete_item():
    
    print_catalog()
    id_d = input('please provide the id to remove: ')

    for item in catalog:
        print(item.id == id_d)
        de
        

#show the catalog
#ask the user to choose an id
#travel the list
#find the item with that id
# delete that item from the list



# instructions
deserialize_catalog()

opc = ''
while (opc != 'x'):
    clear()
    print_menu()

    opc = input('Please select an option: ')

    if (opc == '1'):
        register_item()
        serialize_catalog()
    elif(opc == '2'):
        print_catalog()
    elif(opc == '3'):
        print_stock_empty()
    elif(opc == '4'):
        delete_item()
    elif(opc == '7'):
        print_value_total()

    input('Press enter to continue...')

print("Thank you, Good bye!")
