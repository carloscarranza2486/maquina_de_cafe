ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\nElige el café que prefieras: ")
    print("1. Espresso")
    print("2. Cappuccino")
    print("3. Latte") 
    print("4. Americano")
    
    opcion = input("Opción: ")
    
    cafes = {
         "1": "Espresso",
         "2": "Cappuccino",
         "3": "Latte",
         "4": "Americano"
    }
    
    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print("Has pedido un " + cafe_elegido + "¡preparando tu café!")
        
        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("Opción inválida, por favor indique una de las opciones sugeridas")