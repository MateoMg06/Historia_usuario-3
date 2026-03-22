
def show_summary(product):
    # Show each product in a clear line format.
    print("SUMMARY")

    if product == []:
        print("No sales")
        print("Quantity:", 0)
    else:
        for item in product:
            name = item["name"]
            price = item["price"]
            quantity = item["quantity"]
            print(f"Product: {name} | Price: {price} | Quantity: {quantity}")
            
            

        
