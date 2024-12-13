
i=0

cuadrados=[]

for i in range(1,11):
    cuadrados.append(i**2)


print(cuadrados)
    
    
cuadrados=[i**2 for i in range(1,11)]
print(cuadrados)

incremento=[i+10 for i in range(1,6)]
print(incremento)


saludos="Buenos dias, Buenas tardes, Buenas noches"
lista_saludos=saludos.split(",")
print(lista_saludos)

lista_saludos_may=[saludos.upper() for saludos in lista_saludos]
print(lista_saludos_may)

import os 
print(os.listdir("."))


'''guardar los archivos que empiezen por n'''
directorios=[archivo for archivo in os.listdir(".") if archivo.startswith("n") and  archivo.endswith(".py")]
print(directorios)



