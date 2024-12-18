numeros_ganadores = []
cantidad_numeros = int(input("¿Cuántos números ganadores quieres ingresar? "))

for i in range(5):
    numero = int(input(f"Ingrese el número ganador {i + 1}: "))
    numeros_ganadores.append(numero)

numeros_ganadores.sort()
print("Los números ganadores ordenados de menor a mayor son:")
print(numeros_ganadores)