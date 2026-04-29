
from abc import ABC, abstractmethod
from utilidades.errores import DatosInvalidosError

class Servicio():
    def __init__(self,nombre: str,precio_base: float)-> None:
      
        if not nombre or nombre.strip()=="":
            raise DatosInvalidosError("El Nombre no puede estar vacio")
    
        if precio_base<=0:
            self.nombre : str = nombre
            self.precio_base : float = precio_base
            self.disponible : bool = True

    @abstractmethod
    def calcular_costo(self,duracion_horas:int)-> float:
        pass

    @abstractmethod
    def describir(self)-> str:
        pass

class ReservarSala(Servicio):
    def calcular_costo(self, duracion_horas) -> float:
        return self.precio_base * duracion_horas
    
    def  describir(self) -> str:
        return f"servicio de Reserva de Sala:{self.nombre}(Precio base:$-{self.precio_base})"
    
class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion_horas) -> float:
        return self.precio_base * duracion_horas
    
    def  describir(self) -> str:
        return f"Alquiler de Equipo :{self.nombre}"

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, duracion_horas) -> float:
        #REALIZAR: CALCULAR COSTO DE RESERVA
        return self.precio_base * duracion_horas
    
    def  describir(self) -> str:
        return f"Asesoria Especializada:{self.nombre}"
    
