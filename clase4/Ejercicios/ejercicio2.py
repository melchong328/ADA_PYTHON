# Verificación de Elementos en una Tupla 

# Crea una tupla llamada mi_tupla con los siguientes elementos: (3, 6, 9, 12, 15). 
# Verifica si el número 6 está en la tupla y muestra un mensaje indicando si está presente o no. 
# Verifica si el número 7 está en la tupla y muestra un mensaje indicando si está presente o no.

mi_tupla = (3, 6, 9, 12, 15)
numero_buscado = 6

if numero_buscado in mi_tupla:
    indice_del_valor = mi_tupla.index(numero_buscado)
    print(f'El numero {numero_buscado} esta en la tupla.')
else: 
    print(f'El numero {numero_buscado} no esta en la tupla.')

numero_buscado_dos = 7
if numero_buscado_dos in mi_tupla:
    indice_del_valor = mi_tupla.index(numero_buscado_dos)
    print(f'El numero {numero_buscado_dos} esta en la tupla.')
else: 
    print(f'El numero {numero_buscado_dos} no esta en la tupla.')