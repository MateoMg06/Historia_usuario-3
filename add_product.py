


def add_product(inventory,name, price, quatity):

    subtotal = price * quatity

    producto = {
        "nombre": name,
        "precio": price,
        "quantity": quatity,
        "subtotal": subtotal,
        
    }
    inventory.append(producto)
    print("producto agregado")
    return producto

