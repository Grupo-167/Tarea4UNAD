from Clientes import *
from servicios import *
from logger import log_inicio_sesion, log_cierre_sesion, log_evento, log_error, log_advertencia
from simulacion import ejecutar_simulacion
from excepciones import ErrorSistemaFJ



# Listas principales
clientes = []
servicios = []

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

# =========================
# MENU PRINCIPAL
# =========================
def menu():
    log_inicio_sesion()
    while True:
        print("\n===== SISTEMA SOFTWARE FJ =====")
        print("1. Gestionar clientes")
        print("2. Gestionar servicios")  
        print("3. Simulación completa")
        print("4. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":             
            menu_servicios()
        elif opcion == "3":
            # Pasamos la lista de servicios para que la simulación la use
            ejecutar_simulacion(clientes, servicios, []) 
        
        elif opcion == "4":
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
