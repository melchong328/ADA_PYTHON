# Crear un diccionario
persona = {
    'nombre' : 'Emilia',
    'edad' : 33,
    'ciudad' : 'Caba',
    'profesion' : ' Veterinaria'
}

# Imprimir el diccionario original 
print('Diccionario original: ', persona)

# Usamos popItem para eliminar y obtener el ultimo par clave-valor
ultimo_elemento = persona.popitem()

# Imprimir el par clave-valor
print('Ultimo par clave-valor eliminado: ', ultimo_elemento)


# Inprimir despues de usar popitem
print('Diccionario despues de usar popItem: ', persona)
