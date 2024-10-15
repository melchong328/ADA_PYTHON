# Define una lista de números predefinida o pídele al usuario que 
# ingrese los números. 
# Pide al usuario que ingrese un número a buscar.  
# Usa el método count() para determinar cuántas veces aparece el 
# número en la lista. 
# Muestra el resultado. 

lista_usuario = input('Ingrese nueve numeros: ')
print(lista_usuario)
busqueda_numero = (input('Ingrese el numero a buscar: '))
conteo = lista_usuario.count(busqueda_numero)
print(f'El numero {busqueda_numero} aparece {conteo} veces en la lista ')

