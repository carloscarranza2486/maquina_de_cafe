from inventario import hay_ingredientes_suficientes, usar_ingredientes

ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe(archivo=None):
    print("\nElige el café que prefieras: ")
    print("1. Espresso")
    print("2. Cappuccino")
    print("3. Latte") 
    print("4. Americano")
    
    opcion = input("Opción: ").strip()
    
    cafes = {
         "1": "Espresso",
         "2": "Cappuccino",
         "3": "Latte",
         "4": "Americano"
    }
    
    if opcion and opcion in cafes:
        cafe_elegido = cafes[opcion]
        if hay_ingredientes_suficientes(cafe_elegido):
            usar_ingredientes(cafe_elegido)
            print(f"Has pedido un {cafe_elegido} ¡preparando tu café!")
            if archivo:
                archivo.write(cafe_elegido + "\n")
            else:
                with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo_local:
                    archivo_local.write(cafe_elegido + "\n")
        else:
            print(f"No hay ingredientes suficientes para preparar {cafe_elegido}.")
    else:
        print("Opción inválida, por favor indique una de las opciones sugeridas.")
