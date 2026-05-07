from abc import ABC, abstractmethod
from excepciones import (
    ErrorNombreVacio, ErrorEdadInvalida, ErrorEstadoInvalido,
    ErrorClienteNoEncontrado
)
from logger import log_evento, log_error, log_advertencia
# -- agregados los imports de mis archivos

# clase base
class entidad(ABC):
    def __init__(self, nombre):
        self._nombre = nombre  # <---  guardamos el nombre
        
    @abstractmethod
    def mostrar_detalle(self):
        pass
     
#clase hija cliente
class cliente(entidad):
    def __init__(self, nombre,edad,estado):
        super().__init__(nombre)
        self.nombre = nombre   
        self.edad = edad       
        self.estado = estado
    
    def mostrar_detalle(self):
        print(f"Nombre: {self._nombre}, |Edad: {self._edad}, |Estado: {self._estado}")

    # nombre
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or valor.strip() == "":
            raise ErrorNombreVacio()
        self._nombre = valor.strip()
        
        # -- (borrar) Cambios realizados por roussell nova para agregar el manejo de errores
    
    # edad
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, (int, float)):
            from excepciones import ErrorTipoIncorrecto
            raise ErrorTipoIncorrecto("edad", "numérico")
        if valor <= 0:
            raise ErrorEdadInvalida(valor)
        self._edad = valor

        # -- (borrar) Cambios realizados por roussell nova para agregar el manejo de errores
        
    # estado
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, valor):
        if valor.lower() not in ["activo", "inactivo"]:
            raise ErrorEstadoInvalido(valor)
        self._estado = valor.lower()

        # -- (borrar) Cambios realizados por roussell nova para agregar el manejo de errores
        
# funciones de la gestion al cliente

def mostrar_cliente(lista):
    for c in lista:
        c.mostrar_detalle()
        
def agregar_cliente(lista):
    try:
        nombre = input("Nombre: ").strip()
        edad_str = input("Edad: ").strip()
        estado = input("Estado (activo/inactivo): ").strip()

        if not edad_str.isdigit():
            from excepciones import ErrorTipoIncorrecto
            raise ErrorTipoIncorrecto("edad", "número entero positivo")

        nuevo = cliente(nombre, int(edad_str), estado)

    except (ErrorNombreVacio, ErrorEdadInvalida, ErrorEstadoInvalido) as e:
        log_error(f"Intento fallido de agregar cliente", e)
        print(f"  ✘ No se pudo agregar el cliente: {e}")

    except Exception as e:
        log_error("Error inesperado al agregar cliente", e)
        print(f"  ✘ Error inesperado: {e}")

    else:
        lista.append(nuevo)
        log_evento(f"Cliente agregado: {nuevo.nombre}")
        print(" →  ✔ Cliente agregado correctamente.")

    finally:
        print("  → Operación de registro finalizada.")

        # -- (borrar) Cambios realizados por Roussell nova para agregar el manejo de errores
    
def buscar_cliente(lista, nombre):
    for c in lista:
        if c.nombre.lower() == nombre.lower():
            return c
    return None

def eliminar_cliente(lista, nombre):
    try:
        c = buscar_cliente(lista, nombre)
        if c is None:
            raise ErrorClienteNoEncontrado(nombre)
        lista.remove(c)
    except ErrorClienteNoEncontrado as e:
        log_advertencia(f"Intento de eliminar cliente inexistente: {nombre}")
        print(f"  ✘ {e}")
    else:
        log_evento(f"Cliente eliminado: {nombre}")
        print(" →  ✔ Cliente eliminado.")

        # -- (borrar) Cambios realizados por Roussell nova para agregar el manejo de errores

def actualizar_cliente(lista, nombre):
    c = buscar_cliente(lista, nombre)
    if c:
            nuevo_nombre = input("nuevo nombre: ")
            nueva_edad = int(input("nueva edad: "))
            nuevo_estado = input("nuevo estado: ")

            c.nombre = nuevo_nombre
            c.edad = nueva_edad
            c.estado = nuevo_estado
            print("cliente actualizado")
       
    else:
        print("cliente no encontrado")

# Comentario de Rousell nova (Borrar), en espera de actualizacion 
# para agregar los coponentes de manejo de error que cree en excepciones.py,
# crea la logica compañero y yo me encargo de adaptarlo, te esta quedando bien,
# buen trabajo :)
        
    
        
     