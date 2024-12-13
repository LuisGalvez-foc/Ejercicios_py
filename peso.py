peso = int(input("dime que pesas gordito "))

modo= input("esta en KG o Libras escribe o K o L según tu respuesta ")

if modo.lower() == "k" :
    peso =peso
    print(f'tu peso en Kilos es de: {peso}')
elif modo.lower() == "l":
    peso= peso/0.45
    print(f'tu peso en libras es de: {peso}')  
else:
    print("no entiendo que me dices")


