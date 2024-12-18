

frase=input("introduce una frase: ")
frase2 =frase.lower().replace(" ","") 
if(frase2 == frase2[::-1]):
    print("cadena es palindroma")
else:
    print("no lo es")