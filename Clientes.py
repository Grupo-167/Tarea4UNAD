from abc import ABC, abstractmethod

# clase base
class entidad(ABC):
    def __init__(self, nombre):
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
        
# funciones de la gestion al cliente

def mostrar_cliente(lista):
    for c in lista:
        c.mostrar_detalle()
        
def agregar_cliente(lista):
    nombre = input("nombre: ")
    edad = int(input("edad:"))
    estado = input("estado:")
    
    nuevo = cliente(nombre, edad, estado)
    lista.append(nuevo)
    print("cliente agregado")
    
def buscar_cliente(lista, nombre):
    for c in lista:
        if c.nombre.lower() == nombre.lower():
            return c
    return None

def eliminar_cliente(lista, nombre):
    c = buscar_cliente(lista, nombre)
    if c:
        lista.remove(c)
        print("cliente eliminado")
    else:
        print("cliente no encontrado")

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


        
    
        
     