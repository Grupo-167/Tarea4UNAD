from Clientes import *
from servicios import *
from logger import log_inicio_sesion, log_cierre_sesion, log_evento, log_error, log_advertencia
from simulacion import ejecutar_simulacion
from excepciones import ErrorSistemaFJ



# Listas principales
clientes = []
servicios = []
reservas = []

# =========================
# MENU CLIENTES
# =========================
def menu_clientes():
    while True:
        print("\n===== GESTIÓN DE CLIENTES =====")
        print("1. Agregar cliente")
        print("2. Mostrar clientes")
        print("3. Buscar cliente")
        print("4. Actualizar cliente")
        print("5. Eliminar cliente")
        print("6. Volver")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                agregar_cliente(clientes)

            elif opcion == "2":
                mostrar_cliente(clientes)

            elif opcion == "3":
                nombre = input("Nombre a buscar: ")
                c = buscar_cliente(clientes, nombre)
                if c:
                    c.mostrar_detalle()
                else:
                    print("Cliente no encontrado")

            elif opcion == "4":
                nombre = input("Nombre a actualizar: ")
                actualizar_cliente(clientes, nombre)

            elif opcion == "5":
                nombre = input("Nombre a eliminar: ")
                eliminar_cliente(clientes, nombre)

            elif opcion == "6":
                break

            else:
                print("Opción inválida")

        except Exception as e:
            log_error("Error en menú de clientes", e)
            print(f"Error: {e}")

# =========================
# MENU SERVICIOS
# =========================
def menu_servicios():
    while True:
        print("\n===== GESTIÓN DE SERVICIOS =====")
        print("1. Agregar servicio")
        print("2. Mostrar servicios")
        print("3. Eliminar servicio")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                agregar_servicio(servicios)

            elif opcion == "2":
                mostrar_servicios(servicios)

            elif opcion == "3":
                nombre = input("Nombre del servicio: ")
                eliminar_servicio(servicios, nombre)

            elif opcion == "4":
                break

            else:
                print("Opción inválida")

        except Exception as e:
            log_error("Error en menú de servicios", e)
            print(f"Error: {e}")
            
# ==========================================
# MENU RESERVAS
# ==========================================
def menu_reservas():
    while True:
        print("\n===== GESTIÓN DE RESERVAS =====")
        print("1. Crear reserva")
        print("2. Mostrar detalle de reserva")
        print("3. Confirmar reserva")
        print("4. Cancelar reserva")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                # Aquí se asume que tienes acceso a las listas de clientes y servicios
                nombre_c = input("Nombre del cliente para la reserva: ")
                nombre_s = input("Nombre del servicio a reservar: ")
                
                # Buscamos los objetos (estilo similar a buscar_cliente)
                cliente_obj = buscar_cliente(clientes, nombre_c)
                servicio_obj = buscar_servicio(servicios, nombre_s)

                if cliente_obj and servicio_obj:
                    duracion = float(input("Duración en horas: "))
                    # Se crea el objeto reserva
                    nueva_reserva = Reserva(cliente_obj, servicio_obj, duracion)
                    reservas.append(nueva_reserva)
                    print("Reserva creada exitosamente.")
                else:
                    print("Error: Cliente o Servicio no encontrados.")

            elif opcion == "2":
                for r in reservas:
                    r.mostrar_detalle()

            elif opcion == "3":
                nom_res = input("Nombre de la reserva a confirmar: ")
                for r in reservas:
                    if r._nombre.lower() == nom_res.lower():
                        r.confirmar()

            elif opcion == "4":
                nom_res = input("Nombre de la reserva a cancelar: ")
                for r in reservas:
                    if r._nombre.lower() == nom_res.lower():
                        r.cancelar()

            elif opcion == "5":
                break
            else:
                print("Opción inválida")

        except Exception as e:
            log_error("Error en menú de reservas", e)
            print(f"Error: {e}")

# =========================
# MENU PRINCIPAL
# =========================
def menu():
    log_inicio_sesion()
    while True:
        print("\n===== SISTEMA SOFTWARE FJ =====")
        print("1. Gestionar clientes")
        print("2. Gestionar servicios") 
        print("3. Gestionar reservas") 
        print("4. Simulación completa")
        print("5. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":             
            menu_servicios()
        elif opcion == "3":
            menu_reservas()
        elif opcion == "4":
            ejecutar_simulacion(clientes, servicios, []) 
        elif opcion == "5":
            log_evento("Usuario seleccionó salir del sistema")
            log_cierre_sesion()
            print("Saliendo")
            break
        

        else:
            log_advertencia(f"Opción inválida en menú: {opcion}")
            print("Opción inválida")


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        log_error("Fallo catastrófico al iniciar el sistema", e)
        print(f"El sistema no pudo iniciarse: {e}")
