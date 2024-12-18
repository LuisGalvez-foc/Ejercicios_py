def gestionar_facturas():
    facturas = {}  
    total_cobrado = 0  
    total_pendiente = 0 

    while True:
       
        opcion = input("¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ").upper()

        if opcion == 'A':

            numero_factura = input("Introduce el número de la factura: ")
            coste_factura = float(input("Introduce el coste de la factura: "))
            facturas[numero_factura] = coste_factura 
            total_pendiente += coste_factura  
            print(f"Factura añadida: {numero_factura} por un coste de {coste_factura}.")
        
        elif opcion == 'P':
           
            numero_factura = input("Introduce el número de la factura a pagar: ")
            if numero_factura in facturas:
                coste_factura = facturas.pop(numero_factura) 
                total_cobrado += coste_factura  
                total_pendiente -= coste_factura  
                print(f"Factura pagada: {numero_factura} por un coste de {coste_factura}.")
            else:
                print("El número de factura no existe.")
        
        elif opcion == 'T':
            
            print("Terminando el programa.")
            break
        
        else:
            print("Opción no válida. Por favor, elige A, P o T.")

        
        print(f"Total cobrado hasta el momento: {total_cobrado}")
        print(f"Total pendiente de cobro: {total_pendiente}")


gestionar_facturas()