#Ejercicio de Sets y Operaciones Básicas 

#Escribe un programa que: 
#1. Cree dos sets de números. 
#2. Realice operaciones de unión, intersección y diferencia entre estos sets. 
#3. Imprima los resultados de cada operación. 

s1 = {1, 2, 3, 4, 5, 7}
s2 = {6, 7, 8, 9, 10}

union_set = s1.union(s2)

interseccion_set = s1.intersection(s2)

diferencia_s1 = s1.difference(s2)

difereencia_s2= s2.difference(s1)

print('Set 1:', s1)
print('Set 2:', s2)

print('Union de los sets:', union_set)
print('Interseccion de set 1 y set 2:', interseccion_set)
print('Diferencia de set 1 - set 2:', diferencia_s1)
print('Diferencia de set 2 - set 1:', difereencia_s2)
