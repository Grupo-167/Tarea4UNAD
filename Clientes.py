from abc import ABC, abstractmethod

# clase base
class entidad(ABC):
   def __init__(self,nombre):
       self._nombre = nombre
       
       @abstractmethod
       def mostrar_detalle(self):
           pass
     
#clase hija cliente
class cliente(entidad):
    def __init__(self, nombre,edad,estado):
        super().__init__(nombre)
        self._nombre = nombre
        self._edad = edad
        self._estado = estado
    
    def mostrar_detalle(self):
        print(f"Nombre: {self._nombre}, |Edad: {self._edad}, |Estado: {self._estado}")
        
     