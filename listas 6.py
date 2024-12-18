
asignaturas = ["Matemáticas", "Historia", "Ciencias", "Literatura", "Inglés"]


asignaturas_suspensas = []


for asignatura in asignaturas:
    calificacion = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    if calificacion < 5:  
        asignaturas_suspensas.append(asignatura)


print("Las asignaturas que tienes suspensas son:")
for asignatura in asignaturas_suspensas:
    print(asignatura)