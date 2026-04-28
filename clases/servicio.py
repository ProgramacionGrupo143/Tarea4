
from abc import ABC, abstractmethod
from utilidades.errores import DatosInvalidosError

class Servicio():
    def __init__(self,nombre: str,precio_base: float)-> None:
        #REALIZAR : VALIDAR NOMBRE vacio
        #RELIZAR: VALIDADR PRECIO MAYOR A CERO
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
        #REALIZAR: CALCULAR COSTO DE RESERVA
        return 0.0
    
    def  describir(self) -> str:
        return
    
class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion_horas) -> float:
        #REALIZAR: CALCULAR COSTO DE RESERVA
        return 0.0
    
    def  describir(self) -> str:
        return

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, duracion_horas) -> float:
        #REALIZAR: CALCULAR COSTO DE RESERVA
        return 0.0
    
    def  describir(self) -> str:
        return