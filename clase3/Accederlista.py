# Definimos una lista
mi_lista = ["a", "b", "c", "d", "e"]

# Acceso usando indices postivos
primer_elemento = mi_lista[0]
print("primer elemento:", primer_elemento)

segundo_elemento = mi_lista[1]
print("segundo elemento", segundo_elemento)

# Acceso usando indices negativos
ultimo_elemento = mi_lista[-1]
print("ultimo elemento", ultimo_elemento)
penultimo_elemento = mi_lista[-2]
print("penultimo elemento", penultimo_elemento)

# Acceso a la sublista (slicing)
print("sublista (indice 1 a 3): ", mi_lista[1:4])
print("sublista (inicio a 3): ", mi_lista[:3])
print("sublista (indice a 2 a final): ", mi_lista[2:])

# Acceso con paso en slicing
print("sublista con paso 2: ", mi_lista[::2]) 
print("sublista con paso 2 en rango (1 a 4): ", mi_lista[1:4:2])

# Iteracion a traves de una lista
print('Iteracion a traves de la lista: ')
for elemento in mi_lista:
    print(elemento)
