'''version 1'''
n1=8
numero=int(input("dime un numero haber si aciertas"))
if n1==numero:
    print("acertaste")
else:
    print("no acertaste")




'''version 2'''
for i in range(1,11):
    numero=int(input("dime un numero haber si aciertas"))
    if n1==numero:
        print("acertaste")
    else:
        print("no acertaste")

print("este es tu intento",i)



'''verson 3'''

while True:
    
    numero=int(input("dime un numero haber si aciertas"))
    if n1==numero:
        print("acertaste")
        break
    else:
        print("no acertaste")

