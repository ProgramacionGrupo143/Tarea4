from clases.cliente import Cliente
from clases.servicio import Servicio
from clases.reserva import Reserva
from utilidades.logger import registrar_evento

class GestorSitema:
    def __init__(self) -> None:
        self.clientes : list[Cliente] = []
        self.servicios : list[Servicio] = []
        self.reserva : list [Reserva] = []

    def registar_cliente(self,identificacion:str,nombre:str,correo:str)-> Cliente:
        #REALIZAR : crear cliente , agregarlo a lista y retorna
        pass

    def registar_servicio(self,servicio:Servicio)-> None:
        #REALIZAR : agregarlo a lista 
        pass
    def crear_reserva(self,cliente:Cliente,servicio:Servicio,duracion_horas: int)-> Reserva:
        #REALIZAR : crear reserva , agregarlo a lista y retorna
        pass
    def listar_clientes(self)-> list[Cliente]:
        return self.clientes
    
    def listar_servicios(self)-> list[Servicio]:
        return self.servicios

    def listar_reserva(self)-> list[Reserva]:
        return self.reserva
