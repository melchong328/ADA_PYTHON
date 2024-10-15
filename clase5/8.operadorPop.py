# Crear un diccionario
persona = {
    'nombre' : 'Alejandra',
    'edad' : 30,
    'ciudad' : 'Merida'
}

# Usar pop para eliminar la clave y obtener su valor
valor_eliminado = persona.pop('edad')

# Imprimir el valor eliminado y el diccionario resultante
print('valor elimnado: ', valor_eliminado)
print('Diccionario despues de eliminar "edad": ', persona)

# Usar pop con una clave que no existe y un valor por defecto
valor_inexistente = persona.pop('pais', 'no especificado')
print('Valor cuando la clave no existe:', valor_inexistente )