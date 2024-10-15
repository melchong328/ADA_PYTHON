# Contar Ocurrencias de Elementos en un Diccionario Anidado

#1. Crea un diccionario que contenga información sobre tres clubes deportivos, cada uno con una lista de jugadores. 
#o Cada jugador es un diccionario con las claves: nombre y edad. 
#2. Cuenta cuántos jugadores en total tienen cada uno de los clubes 

club_deportes = {
    'Club de Volleyball' : [
        {'nombre' : 'Katia', 'edad' : 25},
        {'nombre' : 'Camila', 'edad' : 30},
        {'nombre' : 'Samanta', 'edad' : 24},
    ],
    'Club de Básquetbol' : [
        {'nombre' : 'Carlos', 'edad' : 25},
        {'nombre' : 'Ignacio', 'edad' : 25},
        {'nombre' : 'Daniel', 'edad' : 25},
    ],
    'Club de Natación' : [
        {'nombre' : 'Alexia', 'edad' : 25},
        {'nombre' : 'Mauro', 'edad' : 25},
        {'nombre' : 'Angie', 'edad' : 25},
    ]
}

Contar_Jugadores = {club: len(jugadores) for club, jugadores in club_deportes.items()}
for club, cantidad in Contar_Jugadores.items():
    print(f'El {club} tiene {cantidad} jugadores.')