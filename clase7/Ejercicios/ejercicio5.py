#Ejercicio de for con enumerate y break/continue 

#Escribe un programa que: 
#1. Itere sobre una lista de nombres de personas. 
#2. Usar enumerate para mostrar el índice y el nombre. 
#3. Saltar los nombres que empiezan con la letra 'A' usando continue. 
#4. Detener la iteración si se encuentra el nombre 'Carlos' usando break. 

nombre_personas = ['Ana', 'Sofia', 'Mar', 'Miguel', 'Carlos', 'Marco', 'Andrea']
print('Iterando sobre la lista de nombres:', nombre_personas)

for indice, nombre in enumerate(nombre_personas):
    print(f'Indice {indice}: {nombre}')

    if nombre.startswith('A'):
        continue


    if nombre == 'Carlos':
        break 

print('\nIteracion terminada')

