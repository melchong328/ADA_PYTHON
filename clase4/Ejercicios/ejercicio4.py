# Manipulación de Tuplas y Comprobación de Índices 

# Crea una tupla llamada frutas con los siguientes elementos:("manzana", "banana", "cereza"). 
# Usa el método index para encontrar la posición de la fruta "banana". 
# Verifica si la fruta "naranja" está en la tupla. Si no está, muestra un mensaje indicando que no está presente. 

frutas = ('manzana', 'banana', 'cereza')

indice_banana = frutas.index('banana')
print('La banana se encuentra en la posicion', indice_banana,)

valor_buscado = 'naranja'

if valor_buscado in frutas:
    indice_del_valor = frutas.index(valor_buscado)
    print(f'La fruta {valor_buscado} se encuenta en la posicion {indice_del_valor} de la tupla')
else:
    print(f'La fruta {valor_buscado} no esta en la tupla.')

# Esta es otra forma, pero no se si es correcta.
fruta_v = 'naranja'
if fruta_v in frutas:
    print('La fruta', fruta_v, 'esta en la tupla.')
else:
    print('La fruta', fruta_v, 'no esta en la tupla.')