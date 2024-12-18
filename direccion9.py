import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host='localhost',
        database='python',
        user='root',
        password='foc_formacion'
    )

def main():
    connection = conectar_db()
    cursor = connection.cursor()

    while True:
        print("Menú:")
        print("1. Añadir cliente")
        print("2. Mostrar cliente")
        print("3. Terminar")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            
            nif = input("Introduce el NIF del cliente: ")
            nombre = input("Introduce el nombre del cliente: ")
            direccion = input("Introduce la dirección del cliente: ")
            telefono = input("Introduce el teléfono del cliente: ")
            correo = input("Introduce el correo del cliente: ")
            preferente = input("¿Es cliente preferente? (s/n): ").lower() == 's'
            
            cursor.execute("""
                INSERT INTO clientes (nif, nombre, direccion, telefono, correo, preferente)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (nif, nombre, direccion, telefono, correo, preferente))
            connection.commit()
            print("Cliente añadido.")

        elif opcion == '2':

            nif = input("Introduce el NIF del cliente a mostrar: ")
            cursor.execute("SELECT * FROM clientes WHERE nif = %s", (nif,))
            cliente = cursor.fetchone()
            if cliente:
                print(f"NIF: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Teléfono: {cliente[3]}, Correo: {cliente[4]}, Preferente: {cliente[5]}")
            else:
                print("Cliente no encontrado.")

        elif opcion == '3':
            print("Terminando el programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

    cursor.close()
    connection.close()

main()