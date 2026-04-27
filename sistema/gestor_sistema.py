from clases.cliente import Cliente
from clases.servicio import Servicio
from clases.reserva import Reserva
from utilidades.logger import registrar_evento

class GestorSitema:
    def __init__(self) -> None:
        self.clientes : list[Cliente] = []
        self.servicios : list[Servicio] = []
        self.reserva : list [Reserva] = []