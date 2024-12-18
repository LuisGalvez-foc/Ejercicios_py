
fruteria = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}


fruta = input("Ingrese la fruta que desea comprar: ").title()
cantidad = int(input("Ingrese la cantidad de kilos que desea comprar: "))


if fruta in fruteria:
    precio = fruteria[fruta]
    total = float(precio * cantidad)
    
    print(f'El precio de {cantidad} kilos de {fruta} es {total} euros.')
else:
    print("La fruta no se encuentra en la frutería.")