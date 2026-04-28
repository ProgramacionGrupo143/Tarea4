from clases.cliente import Cliente
from clases.servicio import Servicio
from utilidades.errores import ReservarInvalidaError


class Reserva:
    def __init__(self,clientes : Cliente,servicio: Servicio,duracion_horas: int)-> None:
        #REALIZAR : Validar duracion mayor a cero
        #REALIZAR : Validar sdervicio disponible
        self.cliente : Cliente = self.cliente
        self.servicio : Servicio = self.servicio
        self.duracion_horas : int = self.duracion_horas
        self.estado : str = "Pendiente"
        self.costo : float = 0.0

    def  confirmar(self)-> None:
        #REALIZAR : Confirmar reserva
        pass

    def cancelar(self)-> None:
        #REALIZAR : cancelar  reserva
        pass


    def monstrar_informacion(self)-> None:
        #REALIZAR : retorna resumen  reserva
        pass
