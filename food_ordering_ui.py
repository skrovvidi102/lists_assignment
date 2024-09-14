#user interface to the main menu
import data
import functions
def show_main_menu():
  current_order = []
  while True:
    print("Solomon diner") #edit to show your name
    print("__________")
    print('Enter', 'N for a new order','|', 'E for edit order', '|', 'X for prepare the check','|', 'Q for quit' )
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      print('This option ends the application')
      break
    elif user_menu_choice in 'Xx':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
    elif user_menu_choice in 'Nn':
      print('This option adds dishes to orders')
      while input('Add a dish? y/n: ') in 'Yy':
        ordered_item = functions.get_item_number()
        current_order.append(ordered_item)
      print('Current order', current_order)
    elif user_menu_choice in 'Ee':
      print('This option edits the current order')
    else:
      print('Incorrect choice.  Goodbye!')
      break




if __name__ == '__main__':
    print(functions.get_item_information('D1'))
    show_main_menu()


