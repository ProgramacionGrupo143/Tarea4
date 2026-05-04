from clases.cliente import Cliente
from clases.servicio import Servicio
from clases.reserva import Reserva
from utilidades.logger import registrar_evento

class GestorSistema:
    def __init__(self) -> None:
        self.clientes : list[Cliente] = []
        self.servicios : list[Servicio] = []
        self.reservas : list [Reserva] = []

    def registrar_cliente(self,identificacion:str,nombre:str,correo:str)-> Cliente:
        cliente: Cliente = Cliente(identificacion,nombre,correo)
        self.clientes.append(cliente)
        registrar_evento(f"Cliente registrado: {cliente.nombre}")
        return cliente


    def registrar_servicio(self,servicio:Servicio)-> None:
        self.servicios.append(servicio)
        registrar_evento(f"Servicio registrado: {servicio.nombre}")

    def crear_reserva(self,cliente:Cliente,servicio:Servicio,duracion_horas: int)-> Reserva:
        reserva: Reserva = Reserva(cliente, servicio, duracion_horas)
        self.reservas.append(reserva)
        registrar_evento(f"Reserva creada para cliente: {cliente.nombre}")
        return reserva

    def listar_clientes(self)-> list[Cliente]:
        return self.clientes
    
    def listar_servicios(self)-> list[Servicio]:
        return self.servicios

    def listar_reserva(self)-> list[Reserva]:
        return self.reservas
