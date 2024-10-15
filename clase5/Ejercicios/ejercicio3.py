# Anidación Básica de Diccionarios 

# 1. Crea un diccionario que represente una persona con las siguientes claves: 
# o Nombre 
# o Edad 
# o Dirección (donde la dirección es otro diccionario con claves: Calle, Ciudad, Código postal) 
# 2. Imprime la ciudad de la dirección.

Persona = {
    "Nombre" : "Mel",
    "Edad" : 21,
    "Dirección" : {
        "Calle" : "Lago Rosa",
        "Ciudad" : "Tijuana",
        "Codigo postal" : 68476
    }
}

Ciudad = Persona["Dirección"]["Ciudad"]
print("La ciudad es: ", Ciudad)
