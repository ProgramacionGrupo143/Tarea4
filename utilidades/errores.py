class ErrorSistema(Exception):
    pass

class DatosInvalidosError(ErrorSistema):
    pass

class ReservarInvalidaError(ErrorSistema):
    pass

class ServicionNoDisponibleError(ErrorSistema):
    pass
