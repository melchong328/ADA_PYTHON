# Ejemplo basico

#Lista de nombres
nombres = ['Ana', 'Luis', 'Carlos']

for indice, nombre in enumerate(nombres):
    print(f'Indice {indice}: {nombre}')

print('\n') #salto de linea


frutas = ['manzana', 'platano', 'uva', 'sandia']
print(frutas)

print('\nRecorrido con for:')
for posicion, fruta in enumerate(frutas, start=101): # start= cuando ponemos eso se empiza a contar desde el numero que colocamos.
    print(f'posicion {posicion} : {fruta}')

#converlo en formato de lista
print('\nConvertido en lista:')
enumerado = list(enumerate(frutas, start=1))
print(enumerado)

