'''generar numero aleatorio y adivinarlo el programa dara pistas si es mayor o menor que el numero ingresado por el usuario'''
import random
numero_aleatorio=random.randint(1,100)
intentos=0
while True:
    numero_usuario=int(input("ingrese un numero del 1 al 100: "))
    intentos+=1
    if numero_usuario==numero_aleatorio:
        print(f"lo lograste en {intentos} intentos")
        break
    elif numero_usuario>numero_aleatorio:
        print("el numero que ingresaste es mayor que el numero aleatorio")
    else:
        print("el numero que ingresaste es menor que el numero aleatorio")