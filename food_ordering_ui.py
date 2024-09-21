#user interface to the main menu
import data
import functions
def show_main_menu():
  current_order = []
  while True:
    print("saketh krovvidi's diner") #edit to show your name
    print("__________")
    print('N for a new order')
    print("C to change the current order")
    print('X for close orders and print the check')
    print('Q for quit')
    user_menu_choice = input('Your input: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
    elif user_menu_choice in 'Cc':
      current_order = change_order(current_order)  # Change items in the order  
    elif user_menu_choice in 'Nn':
      print('New order')
      while input('Add a dish? y/n: ') in 'Yy':
        ordered_item = functions.get_item_number()
        current_order.append(ordered_item)
      print('your Current orders', current_order)  
    else:
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders

def make_order(order):
  print("New order")
  while True:
    
    user_selection = functions.get_item_number()
    if user_selection == 'done':
        break
    # Split user_selection into item_code and quantity
    item_code, quantity = user_selection.split()  
    
    quantity = int(quantity)  # Convert quantity to an integer
    item_name, item_price = functions.get_item_information(item_code)
    item_price = int(item_price)  # Ensure price is an integer
        
    # Append the correct tuple to the order (item_code, item_name, quantity, item_price)
    order.append((item_code, item_name, quantity, item_price))
        
        # Debugging statement to ensure correct values are added to the order
    print(f"Adding to order: {item_code}, {item_name}, {quantity}, {item_price}")
    
  return order

def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)
  
def change_order(order):
    print("Change order")
    functions.display_current_order(order)
    item_code = input("Enter the item code you want to change: ")
    for i, (code, name, qty, price) in enumerate(order):
        if (code+name) == item_code:
            new_quantity = (input(f"Enter new item for {code+name} and quantity: "))
            order[i]=new_quantity
            
            print(order)
            break
    return order



if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()