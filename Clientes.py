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

    # nombre
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre no puede estar vacio")
        self._nombre = valor
    
    # edad
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        if valor <= 0:
            raise ValueError("La edad debe ser mayor a 0")
        self._edad = valor
        
    # estado
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, valor):
        if valor.lower() in ["activo", "inactivo"]:
            self._estado = valor.lower()
        else:
            raise ValueError("Estado no valido")
        
        
    
        
     