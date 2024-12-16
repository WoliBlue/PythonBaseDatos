import pymysql

def conectar_bd():
    try:
        # Conexión a la base de datos
        connection = pymysql.connect(
            host="localhost",  # Cambia esto si tu MySQL está en otro host
            user="roboto",       # Usuario de MySQL
            password="roboto",  # Contraseña de MySQL
            database="funkotienda"  # Nombre de la base de datos
        )
        print("Conexión exitosa a la base de datos.")
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def main():
    # Llamamos a la función para conectarnos a la base de datos
    connection = conectar_bd()

    # Si la conexión fue exitosa, cerramos la conexión
    if connection:
        connection.close()
        print("Conexión cerrada.")

if __name__ == "__main__":
    main()