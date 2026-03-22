from menu import menu_inventory
from validation_menu import validation
from validation_menu import validations
from validation_menu import add_product
from show_summary import show_summary


# Main control flag for the menu loop.
ok=True
# In-memory inventory list (list of dictionaries).
inventory=[]
while ok == True:
  # Show menu and read the selected option.
  menu_inventory()
  opcion=validation()
  if opcion == 1:
      # Add a new product after validating input values.
      name, price, quantity,subtotal = validations()
      add_product(inventory,name, price, quantity,subtotal)
      
      
  elif opcion == 2:
      # Show inventory summary.
      show_summary(inventory)
      
      
  elif opcion == 3:
    # Calculate basic inventory statistics.
    if inventory == []  :
      print("Add something first") 
    else:
      total = 0
      for product in inventory:
          total = total + product["subtotal"]
          products=len(inventory)
      print(f"the total amount of all the products that you add is: {total}\nthe quantity of the product you add is: {products}")
      
  elif opcion == 4:
      # Exit program.
      print("Thanks for using the program")
      ok=False
  else:
      print("Choose a valid option")
