
def validation ():
    
    
    its_ok=True

    while its_ok == True:

        
       
        try:
            menu=int(input("write a option: "))
            if menu <=0:
                print("write a correct number")
                its_ok=True
            elif menu == "":
                print("write something")
                its_ok=True
            else:
                its_ok=False
            
        except ValueError:

            print("Write just a numbers")
            its_ok=True
    
    return menu




def validation_add_product (menu):
    if menu == 1:
        name_ok = False
        while name_ok == False:
            name = input("product name : ").strip().lower()
            try:
                float(name)
                print("Write only letters")
                name_ok = False
            except:
                if name =="":
                    print("write only letters")
                else:
                    name_ok = True

    price_ok = False
    while price_ok == False:
        try:
            price = float(input("Product Price"))
            if price < 0:
                print("price cannot be negative")
                price_ok = False
            else:
                price_ok = True
        except:
            print("Write a number")

    quatity_ok = False

    while quatity_ok == False:
        try:
            quatity = int(input("Quantity: "))
            if quatity < 0:
                print("quantity cannot be negative")
                quatity_ok = False
            else:
                quatity_ok = True

        except:
            print("Write a whole number")
    return name, price, quatity
    
    

  
    




    


    
    



        


            
        
     
    





    
        



