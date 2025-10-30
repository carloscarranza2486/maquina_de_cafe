# inventario.py

ingredientes = {
    "agua": 1000,        # ml
    "leche": 800,        # ml
    "cafe": 500,         # g
}

recetas = {
    "Espresso": {"agua": 50, "cafe": 18},
    "Cappuccino": {"agua": 100, "leche": 100, "cafe": 18},
    "Latte": {"agua": 50, "leche": 150, "cafe": 18},
    "Americano": {"agua": 150, "cafe": 18}
}

def hay_ingredientes_suficientes(nombre_cafe):
    receta = recetas[nombre_cafe]
    for ingrediente, cantidad in receta.items():
        if ingredientes[ingrediente] < cantidad:
            print(f"No hay suficiente {ingrediente} para preparar {nombre_cafe}.")
            return False
    return True

def usar_ingredientes(nombre_cafe):
    receta = recetas[nombre_cafe]
    for ingrediente, cantidad in receta.items():
        ingredientes[ingrediente] -= cantidad
