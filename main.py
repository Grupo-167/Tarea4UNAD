from clientes import *
from clientes import actualizar_cliente
from clientes import eliminar_cliente
from clientes import buscar_cliente
from clientes import mostrar_cliente

from logger import log_inicio_sesion, log_cierre_sesion, log_evento, log_error, log_advertencia
from simulacion import ejecutar_simulacion
from excepciones import ErrorSistemaFJ
# -- (borrar) agregados los imports de mis archivos

# Lista principal
clientes = []

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
# MENU PRINCIPAL
# =========================
def menu():
    log_inicio_sesion()
    while True:
        print("\n===== SISTEMA SOFTWARE FJ =====")
        print("1. Gestionar clientes")
        print("2. Simulación completa")
        print("3. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            menu_clientes()

        elif opcion == "2":
            ejecutar_simulacion(clientes, [], [])

        elif opcion == "3":
            log_evento("Usuario seleccionó salir del sistema")
            log_cierre_sesion()
            print("Saliendo")
            break

        else:
            log_advertencia(f"Opción inválida en menú: {opcion}")
            print("Opción inválida")

            # -- (borrar) Cambios realizados por Roussell nova para agregar los logs 
            #    Tambien se borro la anterior simulacion pueto que existe la nueva

# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        log_error("Fallo catastrófico al iniciar el sistema", e)
        print(f"El sistema no pudo iniciarse: {e}")

        # -- (borrar)cambios realizados por roussell para agregar el
        # maneo de errores y evitar caidas inesperadas