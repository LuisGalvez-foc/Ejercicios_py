

divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input("Ingrese la divisa que desee: ").capitalize()

if divisa in divisas:
    print("si existe")
else:
    print("no existe")  

