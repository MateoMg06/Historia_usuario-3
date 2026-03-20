from menu import menu_inventory
from validation_menu import validation
from validation_menu import validation_add_product
from add_product import add_product
inventory=[]
menu_inventory()
opcion=validation()
name, price, quantity=validation_add_product(opcion)


print(add_product(inventory,name,price,quantity))





