## **Tarea4UNAD**
Tarea #4 de Programacion — Curso: Programación 213023 | UNAD  
Programa: Ingeniería de Sistemas | Escuela ECBTI

---

## Integrantes del equipo

| # | Integrante | Responsabilidad |
|---|-----------|-----------------|
| 1 | Jesús Leandro | Módulo de Clientes (POO) |
| 2 | Andres Moreno | Módulo de Servicios (POO) |
| 3 | Julio César | Módulo de Reservas |
| 4 | Roussell Nova | Manejo de errores, logs y pruebas |
| 5 | Dioicelis Puertas | Construccion y estandarizacion de main.py|

---

## Estructura del proyecto

```
Tarea4UNAD/
├── main.py            # Menú principal y punto de entrada
├── Clientes.py        # Clase Cliente y gestión de clientes
├── servicios.py       # Clases de servicios y reservas
├── excepciones.py     # Excepciones personalizadas del sistema
├── logger.py          # Sistema centralizado de registro de eventos
├── simulacion.py      # Batería de 12 operaciones simuladas
└── sistema_fj.log     # Archivo de logs (generado automáticamente)
```

---

## Cómo ejecutar el sistema

```bash
python main.py
```

El sistema presenta un menú con las siguientes opciones:

```
===== SISTEMA SOFTWARE FJ =====
1. Gestionar clientes
2. Gestionar servicios
3. Simulación completa
4. Salir
```

---

## Cómo evidenciar las 10 operaciones completas

Al ejecutar `main.py`, seleccionar la opción **3 — Simulación completa**.

El sistema ejecutará automáticamente **12 operaciones** que cubren todos los requisitos del enunciado. Cada operación se muestra en consola y queda registrada en `sistema_fj.log`.

### Tabla de operaciones

| OP | Descripción | Tipo | Resultado esperado |
|----|-------------|------|--------------------|
| 01 | Registrar cliente válido: Juan Pérez, 30, activo | Registro válido | ✔ Cliente registrado |
| 02 | Registrar cliente con edad inválida: Ana, -5 | Registro inválido | ✘ ErrorEdadInvalida [E002] |
| 03 | Registrar cliente con estado incorrecto: suspendido | Registro inválido | ✘ ErrorEstadoInvalido [E003] |
| 04 | Registrar cliente con nombre vacío | Registro inválido | ✘ ErrorNombreVacio [E001] |
| 05 | Registrar segundo cliente válido: María López, 45 | Registro válido | ✔ Cliente registrado |
| 06 | Actualizar edad de Juan Pérez a 31 | Actualización válida | ✔ Cliente actualizado + bloque finally |
| 07 | Buscar cliente inexistente: Carlos | Búsqueda fallida | ✘ ErrorClienteNoEncontrado [E004] + bloque else |
| 08 | Reservar servicio no disponible: Sala VIP | Servicio inválido | ✘ ErrorServicioNoDisponible [E005] + encadenamiento |
| 09 | Crear reserva con duración inválida: -2 horas | Reserva inválida | ✘ ErrorDuracionInvalida [E006] |
| 10 | Confirmar reserva ya cancelada | Operación no permitida | ✘ ErrorReservaCancelada [E008] + bloque finally |
| 11 | Crear cliente sin proporcionar estado | Parámetro faltante | ✘ ErrorParametroFaltante [E009] |
| 12 | Mostrar listado final de clientes registrados | Consulta válida | ✔ Listado mostrado |

### Técnicas de manejo de excepciones demostradas

| Técnica | Operación donde se evidencia |
|---------|------------------------------|
| `try / except` | OP02, OP03, OP04, OP08, OP11 |
| `try / except / else` | OP07 |
| `try / except / finally` | OP10 |
| `try / except / else / finally` | OP06 |
| Encadenamiento `raise X from Y` | OP08 |
| Captura múltiple en un `except` | OP06 |
| Excepciones personalizadas | OP01 al OP12 (todas) |

---

## Evidencia en el archivo de logs

Cada operación queda registrada automáticamente en `sistema_fj.log`. Ejemplo de salida tras ejecutar la simulación:

```
2026-05-11 21:15:07 | INFO     | NUEVA SESIÓN INICIADA
2026-05-11 21:15:12 | INFO     | OP01 | Cliente válido registrado: Juan Pérez
2026-05-11 21:15:12 | ERROR    | OP02 | Edad inválida rechazada | ErrorEdadInvalida: [Código E002]
2026-05-11 21:15:12 | ERROR    | OP03 | Estado inválido rechazado | ErrorEstadoInvalido: [Código E003]
2026-05-11 21:15:12 | ERROR    | OP04 | Nombre vacío rechazado | ErrorNombreVacio: [Código E001]
2026-05-11 21:15:12 | INFO     | OP05 | Cliente válido registrado: María López
2026-05-11 21:15:12 | INFO     | OP06 | Cliente actualizado: Juan Pérez → edad 31
2026-05-11 21:15:12 | WARNING  | OP07 | Búsqueda sin resultado
2026-05-11 21:15:12 | ERROR    | OP08 | Servicio no disponible al reservar
2026-05-11 21:15:12 | ERROR    | OP09 | Duración inválida rechazada
2026-05-11 21:15:12 | ERROR    | OP10 | Intento de operar reserva cancelada
2026-05-11 21:15:12 | ERROR    | OP11 | Parámetro faltante al crear cliente
2026-05-11 21:15:12 | INFO     | OP12 | Listado de 2 cliente(s) mostrado
```

---

## Bitácora de avances — Roussell Nova (Persona 4)

### [v0.1] — 03/05/2026 — Primera intervención

**`excepciones.py`**
Se creó una jerarquía completa de excepciones personalizadas partiendo de la clase base `ErrorSistemaFJ`. Se definieron diez excepciones específicas con código identificador único (E001–E010):

| Código | Excepción | Descripción |
|--------|-----------|-------------|
| E001 | ErrorNombreVacio | Nombre de cliente vacío o solo espacios |
| E002 | ErrorEdadInvalida | Edad menor o igual a cero |
| E003 | ErrorEstadoInvalido | Estado diferente de activo/inactivo |
| E004 | ErrorClienteNoEncontrado | Cliente no encontrado en la lista |
| E005 | ErrorServicioNoDisponible | Servicio marcado como inactivo |
| E006 | ErrorDuracionInvalida | Duración de reserva no positiva |
| E007 | ErrorReservaInvalida | Reserva con datos inconsistentes |
| E008 | ErrorReservaCancelada | Operación sobre reserva cancelada |
| E009 | ErrorParametroFaltante | Parámetro obligatorio no proporcionado |
| E010 | ErrorTipoIncorrecto | Tipo de dato incorrecto en un campo |

**`logger.py`**
Se implementó el sistema centralizado de registro de eventos usando el módulo `logging` de Python. Los eventos quedan almacenados en `sistema_fj.log` con marca de tiempo y nivel de severidad. Se definieron cuatro niveles de log exportados a todos los módulos del equipo: `log_evento`, `log_error`, `log_advertencia` y `log_critico`.

**`Clientes.py` (modificado)**
Se reemplazaron los `ValueError` genéricos de los setters por excepciones personalizadas. Se refactorizaron las funciones `agregar_cliente`, `eliminar_cliente` y `actualizar_cliente` incorporando bloques `try/except/else/finally` y registro de auditoría en el log.

### [v0.2] — 04/05/2026 — Integración en el sistema

**`simulacion.py`**
Se creó la batería de 12 operaciones simuladas que demuestran el comportamiento del sistema ante datos válidos e inválidos. El archivo está diseñado para ejecutarse en cada commit y generar trazabilidad en el log.

**`main.py` (modificado)**
Se integraron los módulos `logger` y `simulacion` en el menú principal. Se agregó registro de inicio y cierre de sesión, captura global de errores inesperados y protección contra caídas al arrancar la aplicación.
