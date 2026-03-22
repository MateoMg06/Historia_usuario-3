
inventory=[]
        
def validation ():
    # Validate the selected menu option.
    its_ok=True

    while its_ok == True:

        
       
        try:
            menu=int(input("Write an option: "))
            if menu <=0:
                print("Write a valid number")
                its_ok=True
            elif menu == "":
                print("Write something")
                its_ok=True
            else:
                its_ok=False
            
        except ValueError:

            print("Write numbers only")
            its_ok=True
    
    return menu




def validations ():
        # Validate product name, price, and quantity.
        name_ok = False
        while name_ok == False:
            name = input("Product name: ").strip().lower()
            try:
                float(name)
                print("Write only letters")
                name_ok = False
            except:
                if name =="":
                    print("Write only letters")
                else:
                    name_ok = True
                    
        
        price_ok = False
        while price_ok == False:
            try:
                price = float(input("Product price: "))
                if price < 0:
                    print("Price cannot be negative")
                    price_ok = False
                else:
                    price_ok = True
            except:
                print("Write a number")

        quantity_ok = False

        while quantity_ok == False:
            try:
                quantity = int(input("Quantity: "))
                if quantity < 0:
                    print("Quantity cannot be negative")
                    quantity_ok = False
                else:
                    quantity_ok = True
            except:
                print("Write a whole number")
                
        subtotal = price * quantity
        


        return name, price, quantity,subtotal

def add_product(inventory,name, price, quantity,subtotal):
            # Build and save a product dictionary in the inventory list.
            product = {
                "name": name,
                "price": price,
                "quantity": quantity,
                "subtotal": subtotal,
                
            }
            inventory.append(product)
            print("Product added")
            return product,inventory

        

        
            



    
    


            
        

  
    




    


    
    



        


            
        
     
    





    
        



