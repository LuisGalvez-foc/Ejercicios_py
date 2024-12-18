

palabra = input("Ingresa una palabra: ").lower()


contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0


for letra in palabra:
    if letra == 'a':
        contador_a += 1
    elif letra == 'e':
        contador_e += 1
    elif letra == 'i':
        contador_i += 1
    elif letra == 'o':
        contador_o += 1
    elif letra == 'u':
        contador_u += 1


print(f"La vocal 'a' se repite {contador_a} veces.")
print(f"La vocal 'e' se repite {contador_e} veces.")
print(f"La vocal 'i' se repite {contador_i} veces.")
print(f"La vocal 'o' se repite {contador_o} veces.")
print(f"La vocal 'u' se repite {contador_u} veces.")