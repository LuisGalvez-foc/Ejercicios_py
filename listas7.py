

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

abecedario_nuevo = []

for i in range(len(abecedario)):
    if i % 3 !=0:
        abecedario_nuevo.append(abecedario[i])
        print(abecedario_nuevo)