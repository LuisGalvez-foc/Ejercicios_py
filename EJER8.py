'''factorial de un numero '''
n=int(input("dime un numero y te calculo el factorial"))
factorial=1
for i in range(1,n+1):
    factorial*=i
    print(f"el factorial de {n} es {factorial}")



