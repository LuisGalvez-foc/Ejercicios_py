
datos={}
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
direccion=input("Ingrese su direccion: ")
telefono=int(input("Ingrese su telefono: "))
datos={"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":telefono}

print(f'{nombre} tiene {edad} vive en {direccion} y su número de teléfono es {telefono}')