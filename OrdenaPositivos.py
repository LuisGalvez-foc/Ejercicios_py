
lista_numeros=[1,2,3,4,-5,6,7,8,9,10,-1,-2,-3]

def OrdenaPositivos(lista_numeros):
    '''ordenar los numeros positivos de menor a mayor y dejar los negativos en la posicion original'''
    lista_positivos=sorted([num for num in lista_numeros if num>0])
    print(lista_positivos)

OrdenaPositivos(lista_numeros)

lista_numeros = [1, 2, 3, 4, -5, 6, 7, 8, 9, 10, -1, -2, -3]

def OrdenaPositivos(lista_numeros):
    '''Ordena los números positivos de menor a mayor y deja los negativos en su posición original'''
    lista_positivos = sorted([num for num in lista_numeros if num > 0]) 
    lista_final = []  
    pos = 0 

    for num in lista_numeros:
        if num > 0:
            lista_final.append(lista_positivos[pos])  
            pos += 1 
        else:
            lista_final.append(num)  
    
    return lista_final

resultado = OrdenaPositivos(lista_numeros)
print(resultado)
