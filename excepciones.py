class ErrorSistemaFJ(Exception):
    # Excepción personalizada para el sistema de
    def __init__(self, mensaje, codigo=None):
        super().__init__(mensaje)
        self.codigo = codigo

    def __str__(self):
        base = super().__str__()
        if self.codigo:
            return f"[Código {self.codigo}] {base}"
        return base

class ErrorNombreVacio(ErrorSistemaFJ):
        # Excepción específica para el caso de nombre vacío
    def __init__(self):
        super().__init__("El nombre no puede estar vacío.", codigo="E001")

class ErrorEdadInvalida(ErrorSistemaFJ):
# Excepción específica para el caso de edad inválida
    def __init__(self, valor):
        super().__init__(
            f"La edad '{valor}' no es válida. Debe ser un número mayor a 0.",
            codigo="E002"
        )
        self.valor = valor

class ErrorEstadoInvalido(ErrorSistemaFJ):
# Excepción específica para el caso de estado inválido
    def __init__(self, valor):
        super().__init__(
            f"El estado '{valor}' no es válido. Use 'activo' o 'inactivo'.",
            codigo="E003"
        )
        self.valor = valor

class ErrorClienteNoEncontrado(ErrorSistemaFJ):
    # Excepción específica para el caso de cliente no encontrado
    def __init__(self, nombre):
        super().__init__(
            f"No se encontró ningún cliente con el nombre '{nombre}'.",
            codigo="E004"
        )
        self.nombre = nombre

class ErrorServicioNoDisponible(ErrorSistemaFJ):
    # Excepción específica para el caso de servicio no disponible
    def __init__(self, servicio):
        super().__init__(
            f"El servicio '{servicio}' no está disponible en este momento.",
            codigo="E005"
        )
        self.servicio = servicio

class ErrorDuracionInvalida(ErrorSistemaFJ):
# Excepción específica para el caso de duración inválida
    def __init__(self, valor):
        super().__init__(
            f"La duración '{valor}' no es válida. Debe ser un número positivo.",
            codigo="E006"
        )
        self.valor = valor

class ErrorReservaInvalida(ErrorSistemaFJ):
    # Excepción específica para el caso de reserva inválida
    def __init__(self, mensaje):
        super().__init__(mensaje, codigo="E007")

class ErrorReservaCancelada(ErrorSistemaFJ):
# Excepción específica para el caso de operación sobre reserva cancelada
    def __init__(self):
        super().__init__(
            "No se puede operar sobre una reserva que ya fue cancelada.",
            codigo="E008"
        )


class ErrorParametroFaltante(ErrorSistemaFJ):
# Excepción específica para el caso de parámetro obligatorio faltante
    def __init__(self, parametro):
        super().__init__(
            f"El parámetro '{parametro}' es obligatorio y no fue proporcionado.",
            codigo="E009"
        )
        self.parametro = parametro

class ErrorTipoIncorrecto(ErrorSistemaFJ):
 # Excepción específica para el caso de tipo de dato incorrecto
    def __init__(self, campo, tipo_esperado):
        super().__init__(
            f"El campo '{campo}' debe ser de tipo {tipo_esperado}.",
            codigo="E010"
        )