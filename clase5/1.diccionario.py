# Ejemplo de diccionario
diccionario_vacio = {}
print('Ejemplo de un diccionario vacio: ', diccionario_vacio)

# Ejemplo basico de un diccionario
persona= {
    'nombre' : 'Maria',
    'edad' : 30,
    'casada' : False,
    'hijo' : ['Ana', 'Luis'], #clave es string y valor es una lista
    'direccion' : { # clave es un string y valor es un diccionario
        'calle' : 'La gran via',
        'ciudad' : 'Madrid'
    }
}
print('Ejemplo de diccionario basico: ', persona)
print(persona['hijo'])

# Ejemplo de diccionario con valores de distintos tipos 
diccionario_mixto = {
    'nombre' : 'Alejandra', 
    1 : [2, 3, 4], # Clave es un entero y valor es un string
    (2, 3) : 'tupla como clave' # claves es una tupla y valor es un string 
}
print('Ejemplo de diccionario mixto: ', diccionario_mixto)