from utilidades.errores import DatosInvalidosError

class Cliente:
    def __init__(self,identificacion : str,nombre:str,correo:str)-> None:
        # REALIZAR : VALIDAR IDENTIFICACION
        # REALIZAR : VALIDAR NOMBRE VACIO
        # REALIZA : VALIDAR CORREO VALIDO
        self.__identificacion : str = identificacion
        self.__nombre : str = identificacion
        self.__correo : str = correo

    @property
    def identificaion(self)-> str:
        return self.__identificacion

    @property
    def nombre(self)-> str:
        return self.__nombre
    
    @property
    def correo(self)-> str:
        return self.__correo
    
    def monstrar_informacion(self)->str:
        # REALIZA : retorna informacion del cliente
        return ""
