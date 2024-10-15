# Gestion de asistentes a un evento
# Crear un programa que administre una lsita de
# asistentes a eventos sin permitir duplicados 
# y que realice operaciones entre dos listas

# Crear conjunto de invitados
invitados_viernes = {'Ana', 'Carlos', 'Pedro', 'Luis', ' Clara'}
invitados_sabado = {'Carlos', 'Luis', 'Sofia', 'Maria', 'Pedro'}

# Mostrar a los invitados unicos que asisten el viernes
print(f'Invitados de viernes: {invitados_viernes}')

# Mostrar a los invitados unicos que asisten el viernes
print(f'Invitados de viernes: {invitados_sabado}')

# Mostrar La union (quine asistio al menos un dia)
todos_asistentes = invitados_sabado.union(invitados_viernes)
print(f'Asistentes de ambos dias: {todos_asistentes}')

# Mostart la interseccion (quien asistio ambos dias)
invitado_ambos_dias = invitados_viernes.intersection(invitados_sabado)
print(f'Asistentes ambos dias: {invitado_ambos_dias}')

#  Mostrar diferencia
solo_viernes = invitados_viernes - invitados_sabado
print(f'Asistentes solo el viernes: {solo_viernes}')


# Agregar un uevo invitado el sabado
invitados_sabado.add("Miguel")
print(f'Invitados del sabado despues de agregar un nuevo invitado: {invitados_sabado}')


# Eliminar un invitado que cancelo 
invitados_sabado.remove("Maria")
print(f'Invitados del sabado despues de eliminar un invitado: {invitados_sabado}')

# Comporbar si Ana asistio el sabado
print(f"Ana asistio el sabado?: {'Ana' in invitados_sabado}")