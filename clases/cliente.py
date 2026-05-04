from utilidades.errores import DatosInvalidosError

class Cliente:
    def __init__(self,identificacion : str,nombre:str,correo:str)-> None:
        if not identificacion or identificacion.strip() == "":
            raise DatosInvalidosError("La identificación no puede estar vacía.")

        if not nombre or nombre.strip() == "":
            raise DatosInvalidosError("El nombre no puede estar vacío.")

        
        if not correo or correo.strip() == "":
            raise DatosInvalidosError("El correo no puede estar vacio")
        
        elif "@" not in correo:
            raise DatosInvalidosError("El correo no es valido, debe contener '@'")
        
        self.__identificacion : str = identificacion
        self.__nombre : str = nombre
        self.__correo : str = correo

    @property
    def identificacion(self)-> str:
        return self.__identificacion

    @property
    def nombre(self)-> str:
        return self.__nombre
    
    @property
    def correo(self)-> str:
        return self.__correo
    
    def mostrar_informacion(self)->str:
        return (
            f"Nombre: {self.__nombre}\n"
            f"Identificacion: {self.__identificacion}\n" 
            f"Correo: {self.__correo}\n"
            )
