import pymysql

# Función que se encarga de conectar con la base de datos.
def connect_to_database():
    try:
         # Conexión con los parámetros de la BD local.
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root', 
            db='funkotienda',
        )
        print("Conexión exitosa, feliz año profe")
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
# Función DML que se encarga de insertar
def insertar_registro(tabla, valores):
    conn = None
    try:
        conn = connect_to_database()
        if conn:
            cur = conn.cursor()

            # Aquí definimos las consultas de inserción dependiendo de la tabla.
            if tabla == "cliente":
                query = f"INSERT INTO {tabla} (num_socio, dni, prestigio, nombre, apellidos) VALUES (%s, %s, %s, %s, %s)"
            elif tabla == "dependiente":
                query = f"INSERT INTO {tabla} (dependiente_id, dni, nombre, apellidos, gerente_id, Jefe_jefe_id) VALUES (%s, %s, %s, %s, %s, %s)"
            elif tabla == "jefe":
                query = f"INSERT INTO {tabla} (jefe_id, nombre, apellidos, DNI) VALUES (%s, %s, %s, %s)"
            elif tabla == "distribuidor":
                query = f"INSERT INTO {tabla} (cif, nombre_empresa, frecuencia_entrega_mes) VALUES (%s, %s, %s)"
            elif tabla == "funkopop":
                query = f"INSERT INTO {tabla} (funko_id, funko_nombre, funko_franquicia, funko_fecha, funko_cantidad, funko_precio) VALUES (%s, %s, %s, %s, %s, %s)"
            elif tabla == "gamemaster":
                query = f"INSERT INTO {tabla} (master_id, dni, nombre, apellidos, Jefe_jefe_id) VALUES (%s, %s, %s, %s, %s)"
            elif tabla == "juegomesa":
                query = f"INSERT INTO {tabla} (juegomesa_id, sistema, precio, genero, cantidad) VALUES (%s, %s, %s, %s, %s)"
            elif tabla == "partidarol":
                query = f"INSERT INTO {tabla} (partida_id, fecha, num_participantes, GameMaster_master_id, JuegoMesa_juegomesa_id) VALUES (%s, %s, %s, %s, %s)"

            cur.execute(query, valores)
            conn.commit()
            print("Registro insertado correctamente")

    except Exception as e:
        print(f"Error al insertar el registro: {e}")

    finally:
        if conn:
            conn.close()

# Función para actualizar registros en la tabla indicada.
def actualizar_registro(tabla, valores, condicion):
    conn = None
    try:
        conn = connect_to_database()
        if conn:
            cur = conn.cursor()

            # Montamos la consulta UPDATE con los valores y la condición recibidos.
            query = f"UPDATE {tabla} SET {valores} WHERE {condicion}"
            
            # Commit del Update
            cur.execute(query)
            conn.commit()
            print("Registro actualizado correctamente")

    except Exception as e:
        print(f"Error al actualizar el registro: {e}")

    finally:
        if conn:
            conn.close()

# Función para borrar un registro según la condición dada.
def eliminar_registro(tabla, condicion):
    conn = None
    try:
        conn = connect_to_database()
        if conn:
            cur = conn.cursor()

            # Montamos la consulta Delete con los valores y la condición recibidos.
            query = f"DELETE FROM {tabla} WHERE {condicion}"
            
            # Ejecutar la consulta de borrado
            cur.execute(query)
            conn.commit()
            print("Registro borrado correctamente")

    except Exception as e:
        print(f"Error al borrar el registro: {e}")

    finally:
        if conn:
            conn.close()
# Función que muestra el menú
def menu():
    print("Menú Principal:")
    print("1. Conectar a la base de datos")
    print("2. Inserción de registros")
    print("3. Actualización de registros")
    print("4. Borrado de registros")
    print("5. Consultas")
    print("6. Salir")
    boton = input("Selecciona una opción: ")
    return boton
# Función que muestra el submenú de consultas dentro del menu principal
def menuConsultas():
    print("Menú de Consultas:")
    print("1. Select All")
    print("2. Consulta con Join de varias tablas")
    print("3. Consulta de group by")
    print("4. Consulta con Where y like")
    print("5. Salir")
    boton = input("Selecciona una opción: ")
    return boton
# Funcion que pide el nombre de la tabla para a continuación mostrarla por pantalla
def select_all(tabla):
    conn = None
    try:
        conn = connect_to_database()
        if conn:
            cur = conn.cursor()

            # Consulta SELECT * FROM tabla
            query = f"SELECT * FROM {tabla}"
            cur.execute(query)
            output = cur.fetchall()

            if output:
                for row in output:
                    print(row)
            else:
                print(f"No se encontraron registros en la tabla '{tabla}'.")

    except Exception as e:
        print(f"Error al realizar la consulta: {e}")
    finally:
        if conn:
            conn.close()
#Funcion que realiza un JOIN entre cliente y el ID de los funkopops que tienen
def join_tables():
    conn = None
    try:
        conn = connect_to_database()
        if conn:
            cur = conn.cursor()

            # Consulta JOIN entre cliente y funkopop_cliente
            query = """
            SELECT cliente.nombre, cliente.apellidos, funkopop_cliente.FunkoPop_funko_id
            FROM cliente
            JOIN funkopop_cliente ON cliente.num_socio = funkopop_cliente.Cliente_num_socio
            """
            cur.execute(query)
            output = cur.fetchall()

            if output:
                print("Resultado de la consulta JOIN:")
                for row in output:
                    print(f"Cliente: {row[0]} {row[1]}, ID FunkoPop: {row[2]}")
            else:
                print("No se encontraron registros en la consulta JOIN.")

    except Exception as e:
        print(f"Error al realizar la consulta JOIN: {e}")
    finally:
        if conn:
            conn.close()
#Funcion que realiza un Group by
def group_by_query():
    conn = None
    try:
        conn = connect_to_database()
        if conn:
            cur = conn.cursor()

            # Consulta que mediante Group by agrupa por franquicias y cuenta cuantos funkos hay en cada una
            query = """
            SELECT funko_franquicia, COUNT(funko_franquicia)
            FROM funkopop
            GROUP BY funko_franquicia
            """
            cur.execute(query)
            output = cur.fetchall()

            if output:
                for row in output:
                    print(row)
            else:
                print("No se encontraron registros en la consulta GROUP BY.")

    except Exception as e:
        print(f"Error al realizar la consulta GROUP BY: {e}")
    finally:
        if conn:
            conn.close()
# Funcion que utiliza la condición like dentro de un WHERE
def where_like_query():
    conn = None
    try:
        conn = connect_to_database()
        if conn:
            cur = conn.cursor()

            # Ejemplo de consulta WHERE y LIKE donde buscamos por nombre o apellido a nuestro Cliente 
            condicionwhere = input("""Esta consulta busca por parecido el nombre o el apellido del cliente
                                   Introduce el nombre o apellido deseado a buscar:  """)
            query = f"""
            SELECT * FROM cliente
            WHERE nombre LIKE '%{condicionwhere}%' OR apellidos LIKE '%{condicionwhere}%'
            """
            cur.execute(query)
            output = cur.fetchall()

            if output:
                for row in output:
                    print(row)
            else:
                print(f"No se encontraron registros que coincidan con '{condicionwhere}'.")

    except Exception as e:
        print(f"Error al realizar la consulta WHERE y LIKE: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    while True:
        boton = menu()
        if boton == '1':
            connect_to_database()
        elif boton == '2':
            tabla = input("Dime el nombre de la tabla: ")
            if tabla == "cliente":
                valores = (
                    input("num_socio: "),
                    input("dni: "),
                    input("prestigio: "),
                    input("nombre: "),
                    input("apellidos: ")
                )
                insertar_registro(tabla, valores)
            elif tabla == "dependiente":
                valores = (
                    input("dependiente_id: "),
                    input("dni: "),
                    input("nombre: "),
                    input("apellidos: "),
                    input("gerente_id: "),
                    input("Jefe_jefe_id: ")
                )
                insertar_registro(tabla, valores)
            elif tabla == "jefe":
                valores = (
                    input("jefe_id: "),
                    input("nombre: "),
                    input("apellidos: "),
                    input("DNI: ")
                )
                insertar_registro(tabla, valores)
            elif tabla == "distribuidor":
                valores = (
                    input("cif: "),
                    input("nombre_empresa: "),
                    input("frecuencia_entrega_mes: ")
                )
                insertar_registro(tabla, valores)
            elif tabla == "funkopop":
                valores = (
                    input("funko_id: "),
                    input("funko_nombre: "),
                    input("funko_franquicia: "),
                    input("funko_fecha: "),
                    input("funko_cantidad: "),
                    input("funko_precio: ")
                )
                insertar_registro(tabla, valores)
            elif tabla == "gamemaster":
                valores = (
                    input("master_id: "),
                    input("dni: "),
                    input("nombre: "),
                    input("apellidos: "),
                    input("Jefe_jefe_id: ")
                )
                insertar_registro(tabla, valores)
            elif tabla == "juegomesa":
                valores = (
                    input("juegomesa_id: "),
                    input("sistema: "),
                    input("precio: "),
                    input("genero: "),
                    input("cantidad: ")
                )
                insertar_registro(tabla, valores)
            elif tabla == "partidarol":
                valores = (
                    input("partida_id: "),
                    input("fecha: "),
                    input("num_participantes: "),
                    input("GameMaster_master_id: "),
                    input("JuegoMesa_juegomesa_id: ")
                )
                insertar_registro(tabla, valores)
        elif boton == '3':
            tabla = input("Dime el nombre de la tabla: ")
            valores = input("Dime los valores a actualizar (ejemplo 'funko_cantidad = 56'): ")
            condicion = input("Dime de donde pillamos para actualizar (ejemplo 'funko_id = 55'): ")
            actualizar_registro(tabla, valores, condicion)
        elif boton == '4':
            tabla = input("Dime el nombre de la tabla: ")
            condicion = input("Dime de donde pillamos para borrar (ejemplo 'funko_id = 55'): ")
            eliminar_registro(tabla, condicion)
        elif boton == '5':
            while True:
                boton2 = menuConsultas()
                if boton2 == '1':
                    tabla = input("Dime el nombre de la tabla: ")
                    select_all(tabla)
                elif boton2 == '2':
                    join_tables()
                elif boton2 == '3':
                    group_by_query()
                elif boton2 == '4':
                    where_like_query()
                elif boton2 == '5':
                    break
                else:
                    print("Opción no válida.")
        elif boton == '6':
            break
        else:
            print("Opción no válida.")