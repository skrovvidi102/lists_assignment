#user interface to the main menu
import data
import functions
def show_main_menu():
  current_order = []
  while True:
    print("Solomon diner") #edit to show your name
    print("__________")
    print('Enter', 'N for a new order','|', 'X for prepare the check','|', 'Q for quit' )
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
    elif user_menu_choice in 'Nn':
      ordered_item = functions.get_item_number()
      current_order.append(ordered_item)
      print(current_order)
    else:
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders

def make_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)

def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)



if __name__ == '__main__':
    print(functions.get_item_information('D1'))
    show_main_menu()


