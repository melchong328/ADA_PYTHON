contraseña = 'Computadora'
contador = 0
while True:
    contraseña_input = input('Introduzca una Contraseña: ')
    contador +=1

    if contador > 3:
        print('Haz sobrepasado los intentos')
        break

    elif contraseña_input == 'Computadora':
        print('Contraseña Correcta')
        break

    else:
        print('Contraseña Incorrecta, introduzca una Contraseña correcta')

#for numero in range(1,100):
#    if numero %2 ==0:
#        print(numero)
