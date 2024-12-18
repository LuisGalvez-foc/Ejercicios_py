diccionario = {}


palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción : ")

for i in palabras.split(','):
    
    palabra, traduccion = i.split(':')
    diccionario[palabra] = traduccion


while True:
    mas_palabras = input("¿Quieres añadir más palabras y traducciones? (sí/no): ")
    if mas_palabras.lower() == 'sí':

        nuevas_palabras = input("Introduce las nuevas palabras y traducciones en formato palabra:traducción separadas por comas: ")
        for i in nuevas_palabras.split(','):
            palabra, traduccion = i.split(':')
            diccionario[palabra] = traduccion

    elif mas_palabras.lower() == 'no':
        break
    else:
        print("Por favor, responde con 'sí' o 'no'.")


frase = input('Introduce una frase en español: ')

for i in frase.split():
    if i in diccionario:
        print(diccionario[i])
    else:
        print(i)