import random


lista = ['piedra', 'papel', 'tijera']

while True:
    eleccion = random.choice(lista)
    eleccion_usuario = input("Elige piedra, papel o tijera (o escribe 'salir' para terminar): ").lower()

    if eleccion_usuario == 'salir':
        print("Gracias por jugar. ¡Hasta luego!")
        break

    if eleccion_usuario not in lista:
        print("Opción no válida. Por favor, elige piedra, papel o tijera.")
        continue

    print(f'La máquina saca {eleccion} y tú sacas {eleccion_usuario}')

    if eleccion == eleccion_usuario:
        print('Es un empate técnico')

    elif eleccion == 'piedra' and eleccion_usuario == 'papel':
        print('Ya me jodería que no le ganases')

    elif eleccion == 'piedra' and eleccion_usuario == 'tijera':
        print('Fuiste vencido por la computadora, tonto')

    elif eleccion == 'papel' and eleccion_usuario == 'piedra':
        print('Fuiste vencido por la computadora, tonto')

    elif eleccion == 'papel' and eleccion_usuario == 'tijera':
        print('Ya me jodería que no le ganases')

    elif eleccion == 'tijera' and eleccion_usuario == 'piedra':
        print('Ya me jodería que no le ganases')

    elif eleccion == 'tijera' and eleccion_usuario == 'papel':
        print('Fuiste vencido por la computadora, tonto')

    else:
        print("Se ha roto el programa, mucha carga para la patata que tienes")