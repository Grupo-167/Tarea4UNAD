#
# ------------------------------------------------------------------------------
#===========       No tocar -- Archivo de moniotoreo de errores     =============#    
#
#
#
#       Este archivo hace parte de la simulación de operaciones del software 
#       Contiene todas las operaciones que prueban la creación, actualización y manejo 
#       de clientes, servicios y reservas, incluyendo casos con errores controlados para
#       demostrar el manejo de excepciones, se ira actualizando segun los avances.
#
#
#       Por favor no realizar cambios a este archivo, su composicion no afecta 
#       el funcionamiento del sistema, es solo para fines de monitoreo y demostración.
#
#
#===========                                                      =============#
#------------------------------------------------------------------------------
#






from Clientes import cliente as Cliente
from excepciones import *
from logger import log_evento, log_error, log_advertencia, log_inicio_sesion

def ejecutar_simulacion(lista_clientes, lista_servicios, lista_reservas):
    """
    Ejecuta una batería de operaciones simuladas para demostrar el
    funcionamiento del sistema ante datos válidos e inválidos.
    """
    log_inicio_sesion()
    print("\n" + "=" * 60)
    print("   SIMULACIÓN COMPLETA - SISTEMA SOFTWARE FJ")
    print("=" * 60)

    # ── OPERACIÓN 1: Cliente válido ──────────────────────────────────────────
    print("\n[OP 01] Registrar cliente válido: Juan Pérez, 30, activo")
    try:
        c1 = Cliente("Juan Pérez", 30, "activo")
        lista_clientes.append(c1)
        log_evento("OP01 | Cliente válido registrado: Juan Pérez")
        print("  ✔ Cliente registrado correctamente.")
    except ErrorSistemaFJ as e:
        log_error("OP01 | Fallo inesperado al crear cliente válido", e)
        print(f"  ✘ Error: {e}")

    # ── OPERACIÓN 2: Cliente con edad negativa ───────────────────────────────
    print("\n[OP 02] Registrar cliente con edad inválida: Ana, -5, activo")
    try:
        c2 = Cliente("Ana", -5, "activo")
        lista_clientes.append(c2)
    except ErrorEdadInvalida as e:
        log_error("OP02 | Edad inválida rechazada", e)
        print(f"  ✘ Error controlado: {e}")
    except ErrorSistemaFJ as e:
        log_error("OP02 | Error del sistema", e)
        print(f"  ✘ Error: {e}")

    # ── OPERACIÓN 3: Cliente con estado incorrecto ───────────────────────────
    print("\n[OP 03] Registrar cliente con estado incorrecto: Luis, 28, suspendido")
    try:
        c3 = Cliente("Luis", 28, "suspendido")
        lista_clientes.append(c3)
    except ErrorEstadoInvalido as e:
        log_error("OP03 | Estado inválido rechazado", e)
        print(f"  ✘ Error controlado: {e}")

    # ── OPERACIÓN 4: Cliente con nombre vacío ───────────────────────────────
    print("\n[OP 04] Registrar cliente con nombre vacío")
    try:
        c4 = Cliente("   ", 22, "activo")
        lista_clientes.append(c4)
    except ErrorNombreVacio as e:
        log_error("OP04 | Nombre vacío rechazado", e)
        print(f"  ✘ Error controlado: {e}")

    # ── OPERACIÓN 5: Segundo cliente válido ─────────────────────────────────
    print("\n[OP 05] Registrar segundo cliente válido: María López, 45, inactivo")
    try:
        c5 = Cliente("María López", 45, "inactivo")
        lista_clientes.append(c5)
        log_evento("OP05 | Cliente válido registrado: María López")
        print("  ✔ Cliente registrado correctamente.")
    except ErrorSistemaFJ as e:
        log_error("OP05 | Error al registrar cliente", e)
        print(f"  ✘ Error: {e}")

    # ── OPERACIÓN 6: Actualizar cliente existente ────────────────────────────
    print("\n[OP 06] Actualizar cliente 'Juan Pérez' → nueva edad: 31")
    try:
        objetivo = next((c for c in lista_clientes if c.nombre == "Juan Pérez"), None)
        if objetivo is None:
            raise ErrorClienteNoEncontrado("Juan Pérez")
        objetivo.edad = 31
        log_evento("OP06 | Cliente actualizado: Juan Pérez → edad 31")
        print("  ✔ Cliente actualizado correctamente.")
    except ErrorClienteNoEncontrado as e:
        log_error("OP06 | Cliente no encontrado", e)
        print(f"  ✘ Error: {e}")
    except ErrorEdadInvalida as e:
        log_error("OP06 | Nueva edad inválida", e)
        print(f"  ✘ Error: {e}")
    finally:
        print("  → Bloque finally: operación de actualización finalizada.")

    # ── OPERACIÓN 7: Buscar cliente que no existe ────────────────────────────
    print("\n[OP 07] Buscar cliente inexistente: 'Carlos'")
    try:
        objetivo = next((c for c in lista_clientes if c.nombre == "Carlos"), None)
        if objetivo is None:
            raise ErrorClienteNoEncontrado("Carlos")
        objetivo.mostrar_detalle()
    except ErrorClienteNoEncontrado as e:
        log_advertencia("OP07 | Búsqueda sin resultado")
        print(f"  ✘ Error controlado: {e}")
    else:
        log_evento("OP07 | Cliente encontrado correctamente")
        print("  ✔ Cliente encontrado.")

    # ── OPERACIÓN 8: Servicio no disponible (encadenamiento de excepciones) ──
    print("\n[OP 08] Intentar reservar servicio no disponible")
    try:
        servicio_nombre = "Sala VIP"
        disponible = False  # Simula que el servicio no está activo
        if not disponible:
            try:
                raise ValueError(f"'{servicio_nombre}' está marcado como inactivo en el catálogo.")
            except ValueError as e_origen:
                raise ErrorServicioNoDisponible(servicio_nombre) from e_origen
    except ErrorServicioNoDisponible as e:
        log_error("OP08 | Servicio no disponible al reservar", e)
        print(f"  ✘ Error controlado: {e}")
        if e.__cause__:
            print(f"  → Causa original: {e.__cause__}")

    # ── OPERACIÓN 9: Reserva con duración inválida ───────────────────────────
    print("\n[OP 09] Crear reserva con duración inválida: -2 horas")
    try:
        duracion = -2
        if not isinstance(duracion, (int, float)):
            raise ErrorTipoIncorrecto("duración", "numérico")
        if duracion <= 0:
            raise ErrorDuracionInvalida(duracion)
        log_evento("OP09 | Reserva creada correctamente")
        print("  ✔ Reserva válida.")
    except ErrorDuracionInvalida as e:
        log_error("OP09 | Duración inválida rechazada", e)
        print(f"  ✘ Error controlado: {e}")
    except ErrorTipoIncorrecto as e:
        log_error("OP09 | Tipo incorrecto en duración", e)
        print(f"  ✘ Error: {e}")

    # ── OPERACIÓN 10: Operación sobre reserva cancelada ─────────────────────
    print("\n[OP 10] Confirmar una reserva que ya fue cancelada")
    try:
        estado_reserva = "cancelada"
        if estado_reserva == "cancelada":
            raise ErrorReservaCancelada()
        log_evento("OP10 | Reserva confirmada")
        print("  ✔ Reserva confirmada.")
    except ErrorReservaCancelada as e:
        log_error("OP10 | Intento de operar reserva cancelada", e)
        print(f"  ✘ Error controlado: {e}")
    finally:
        print("  → Bloque finally: intento de confirmación finalizado.")

    # ── OPERACIÓN 11: Parámetro faltante ────────────────────────────────────
    print("\n[OP 11] Crear cliente sin proporcionar estado")
    try:
        estado = None
        if estado is None:
            raise ErrorParametroFaltante("estado")
        c_extra = Cliente("Roberto", 35, estado)
        lista_clientes.append(c_extra)
    except ErrorParametroFaltante as e:
        log_error("OP11 | Parámetro faltante al crear cliente", e)
        print(f"  ✘ Error controlado: {e}")

    # ── OPERACIÓN 12: Mostrar estado final de clientes ───────────────────────
    print("\n[OP 12] Mostrar todos los clientes registrados")
    try:
        if not lista_clientes:
            log_advertencia("OP12 | No hay clientes registrados para mostrar")
            print("  ⚠ No hay clientes registrados.")
        else:
            for c in lista_clientes:
                c.mostrar_detalle()
            log_evento(f"OP12 | Listado de {len(lista_clientes)} cliente(s) mostrado")
    except Exception as e:
        log_error("OP12 | Error inesperado al mostrar clientes", e)
        print(f"  ✘ Error inesperado: {e}")

    print("\n" + "=" * 60)
    print("   SIMULACIÓN FINALIZADA")
    print("=" * 60)
    print("  Revisa el archivo 'sistema_fj.log' para ver el registro completo.")