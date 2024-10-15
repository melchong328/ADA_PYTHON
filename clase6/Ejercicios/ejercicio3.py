# Ejercicio con range, enumerate, y break/continue 

# Escribe un programa que: 
# 1. Itere sobre una lista de cadenas usando enumerate para mostrar el índice y el valor. 
# 2. Utilice continue para saltar cadenas vacías. 
# 3. Utilice break para detener la iteración si se encuentra una cadena con más de 5 caracteres.

colores = ['azul', 'rojo', ' ',  'lila', 'cafe', ' ', 'rosa', 'gris', 'verde']

for indice,nombre_color in enumerate(colores):
    if nombre_color == ' ':
        continue

    elif len(nombre_color) < 5:
        print(f'Indice {indice} : {nombre_color}.')
    else:
        break 
