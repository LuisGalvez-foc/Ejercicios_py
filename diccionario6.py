

persona = {}

while True:
    
    nombre = input("Introduce tu nombre: ")
    persona["nombre"] = nombre
    print(persona)
    respuesta = input("¿Quieres añadir más información (Si/No)? ")
    if respuesta.lower() != "si":
        break

    edad = input("Introduce tu edad: ")
    persona["edad"] = edad
    print(persona)
    respuesta = input("¿Quieres añadir más información (Si/No)? ")
    if respuesta.lower() != "si":
        break

    sexo = input("Introduce tu sexo: ")
    persona["sexo"] = sexo
    print(persona)
    respuesta = input("¿Quieres añadir más información (Si/No)? ")
    if respuesta.lower() != "si":
        break

    teléfono = input("Introduce tu teléfono: ")
    persona["teléfono"] = teléfono
    print(persona)
    respuesta = input("¿Quieres añadir más información (Si/No)? ")
    if respuesta.lower() != "si":
        break

    correo = input("Introduce tu correo: ")
    persona["correo"] = correo
    print(persona)
    respuesta = input("¿Quieres añadir más información (Si/No)? ")
    if respuesta.lower() != "si":
        print("ya no queda mas opciones por añadir")
        break
    

