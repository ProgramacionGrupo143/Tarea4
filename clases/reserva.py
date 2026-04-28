from clases.cliente import Cliente
from clases.servicio import Servicio
from utilidades.errores import ReservarInvalidaError


class Reserva:
    def __init__(self,clientes : Cliente,servicio: Servicio,duracion_horas: int)-> None:
        #REALIZAR : Validar duracion mayor a cero
        if duracion_horas <= 0:
            raise ReservarInvalidaError("La duracion de horas debe ser mayor a cero.")
        
        #REALIZAR : Validar servicio disponible
        if not servicio.disponible:
            raise ReservarInvalidaError("El servicio no está disponible para la reserva.")
        
        self.cliente : Cliente = clientes
        self.servicio : Servicio = servicio
        self.duracion_horas : int = duracion_horas
        self.estado : str = "Pendiente"
        self.costo : float = 0.0

    def  confirmar(self)-> None:
        #REALIZAR : Confirmar reserva
        if self.estado == "Cancelada":
            raise ReservarInvalidaError("No se puede confirmar una reserva cancelada.")
        
        self.estado = "Confirmada"
        self.costo = self.servicio.calcular_costo(self.duracion_horas)
        
    def cancelar(self)-> None:
        #REALIZAR : cancelar  reserva
        if self.estado == "Confirmada":
            raise ReservarInvalidaError("No se puede cancelar una reserva confirmada.")
        
        elif self.estado == "Cancelada":
            raise ReservarInvalidaError("La reserva ya esta cancelada.")
        
        self.estado = "Cancelada"

    def mostrar_informacion(self)-> str:
        #REALIZAR : retorna resumen  reserva
        return (
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion_horas} horas\n"
            f"Estado: {self.estado}\n"
            f"Costo: ${self.costo}\n"
        )
