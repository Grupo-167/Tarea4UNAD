from clientes import *

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
                mostrar_clientes(clientes)

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
            print(f"Error: {e}")

# =========================
# MENU PRINCIPAL
# =========================
def menu():
    while True:
        print("\n===== SISTEMA SOFTWARE FJ =====")
        print("1. Gestionar clientes")
        print("2. Simulación básica")
        print("3. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            menu_clientes()

        elif opcion == "2":
            simulacion()

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

# =========================
# SIMULACIÓN (YA SUMA NOTA)
# =========================
def simulacion():
    print("\n=== SIMULACIÓN ===")

    try:
        # valido
        c1 = Cliente("Juan", 25, "activo")
        clientes.append(c1)
        print("Cliente válido agregado")

        # error edad
        c2 = Cliente("Ana", -5, "activo")
        clientes.append(c2)

    except Exception as e:
        print("Error controlado:", e)

    try:
        # error estado
        c3 = Cliente("Luis", 30, "otro")
        clientes.append(c3)

    except Exception as e:
        print("Error controlado:", e)

    print("\nClientes actuales:")
    mostrar_clientes(clientes)

# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    menu()