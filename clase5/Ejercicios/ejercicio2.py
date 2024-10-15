# Modificar y Eliminar Elementos de un Diccionario 

# 1. Usando el diccionario del ejercicio anterior, actualiza el año de publicación a 1968. 
#2. Elimina el género del diccionario. 
#3. Imprime el diccionario después de cada operación.

Libro = {
    'Titulo' : 'Daisy Jones & the Six',
    'Autor' : 'Taylor Jenkins Reid',
    'Año de publicación' : 2019,
    'Género' : 'Novela'
}

Libro["Año de publicación"] = 1968
print("Libro con año actualizado: ",Libro)


del Libro['Género']
print("Libro despues de eliminar genero: ", Libro)


