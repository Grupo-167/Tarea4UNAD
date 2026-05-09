from datetime import datetime 
from Clientes import entidad 
from abc import ABC, abstractmethod

from logger import log_error
# =========================
# CLASE ABSTRACTA SERVICIO
# =========================
class Servicio(entidad):
    def __init__(self, nombre, precio_base):
        super().__init__(nombre)
        self._precio_base = precio_base
        
    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        pass

    @abstractmethod
    def mostrar_detalle(self):
        pass


# =========================
# CLASE HIJA: RESERVA DE SALA
# =========================
class ReservaSala(Servicio):
    def __init__(self, nombre, precio_base, capacidad):
        super().__init__(nombre, precio_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas, descuento=0):
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")
        return (self._precio_base * horas) - descuento

    def mostrar_detalle(self):
        print(f"[Sala] {self._nombre} | Precio/hora: {self._precio_base} | Capacidad: {self.capacidad}")


# =========================
# CLASE HIJA: ALQUILER EQUIPO
# =========================
class AlquilerEquipo(Servicio):
    def __init__(self, nombre, precio_base, tipo):
        super().__init__(nombre, precio_base)
        self.tipo = tipo

    def calcular_costo(self, dias, seguro=False):
        if dias <= 0:
            raise ValueError("Los días deben ser mayores a 0")

        costo = self._precio_base * dias
        if seguro:
            costo += 50
        return costo

    def mostrar_detalle(self):
        print(f"[Equipo] {self._nombre} | Precio/día: {self._precio_base} | Tipo: {self.tipo}")


# =========================
# CLASE HIJA: ASESORIA
# =========================
class Asesoria(Servicio):
    def __init__(self, nombre, precio_base, especialidad):
        super().__init__(nombre, precio_base)
        self.especialidad = especialidad

    def calcular_costo(self, horas, nivel="normal"):
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")

        if nivel == "premium":
            return self._precio_base * horas * 1.5
        return self._precio_base * horas

    def mostrar_detalle(self):
        print(f"[Asesoría] {self._nombre} | Precio/hora: {self._precio_base} | Especialidad: {self.especialidad}")


# =========================
# FUNCIONES DE GESTION
# =========================

def mostrar_servicios(lista):
    if not lista:
        print("No hay servicios registrados")
    for s in lista:
        s.mostrar_detalle()


def agregar_servicio(lista):
    print("\n1. Reserva de Sala")
    print("2. Alquiler de Equipo")
    print("3. Asesoría")

    opcion = input("Seleccione tipo: ")

    try:
        nombre = input("Nombre: ")
        precio = float(input("Precio base: "))

        if opcion == "1":
            capacidad = int(input("Capacidad: "))
            servicio = ReservaSala(nombre, precio, capacidad)

        elif opcion == "2":
            tipo = input("Tipo de equipo: ")
            servicio = AlquilerEquipo(nombre, precio, tipo)

        elif opcion == "3":
            especialidad = input("Especialidad: ")
            servicio = Asesoria(nombre, precio, especialidad)

        else:
            print("Opción inválida")
            return

        lista.append(servicio)
        print("Servicio agregado correctamente")

    except Exception as e:
        log_error("Error en menú de servicios", e)
        print(f"Error: {e}")


def eliminar_servicio(lista, nombre):
    for s in lista:
        if s.nombre.lower() == nombre.lower():
            lista.remove(s)
            print("Servicio eliminado")
            return
    print("Servicio no encontrado")
    
    
class Reserva(entidad): 
    def __init__(self, cliente, servicio, duracion): 
        nombre_res = f"Reserva_{cliente.nombre}_{servicio._nombre}"
        super().__init__(nombre_res)
        
        
        self.cliente = cliente    
        self.servicio = servicio  
        self.duracion = duracion
        self.estado = "Pendiente"
        self.fecha = datetime.now()

    def mostrar_detalle(self):
        """Muestra el ticket de la reserva con polimorfismo"""
        print(f"\n" + "="*30)
        print(f"   COMPROBANTE: {self._nombre}")
        print(f"="*30)
        print(f"Fecha:    {self.fecha.strftime('%d/%m/%Y %H:%M')}")
        print(f"Cliente:  {self.cliente.nombre}")
        print(f"Estado:   {self.estado}")
        print("-" * 30)
        
        
        self.servicio.mostrar_detalle() 
        
        
        costo_total = self.servicio.calcular_costo(self.duracion)
        
        print(f"Tiempo:   {self.duracion} hora(s)")
        print(f"TOTAL:    ${costo_total}")
        print("="*30)

    def confirmar(self):
        """Cambia el estado a confirmado"""
        self.estado = "Confirmada"
        print(f"Reserva de {self.cliente.nombre} ha sido confirmada.")

    def cancelar(self):
        """Cancela la reserva"""
        self.estado = "Cancelada"
        print(f"Reserva de {self.cliente.nombre} ha sido cancelada.")

    def obtener_resumen(self):
        """Método extra para alargar el código según la guía"""
        return f"Ticket {self._nombre} | Total: ${self.servicio.calcular_costo(self.duracion)}"