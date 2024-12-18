

fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")

dia,mes,año=fecha.split("/")

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

print(f"{dia} de {meses[int(mes)-1]} de {año}")
