from sistema.gestor_sistema import GestorSitema
from clases.servicio import ReservarSala, AlquilerEquipo, AsesoriaEspecializada
from utilidades.logger import registrar_error, registrar_evento

def ejecutar_simulaciones()-> None:
    gestor : GestorSitema = GestorSitema()

    # simulacion # 1
    try:
        cliente_1 = gestor.registar_cliente("1001", "Ana Pérez", "ana@email.com")
        registrar_evento("Simulación 1 correcta: cliente válido.")
    except Exception as error:
        registrar_error(f"Simulación 1 fallida: {error}")


    # simulacion # 2
    try:
        gestor.registar_cliente("", "Carlos", "carlos@email.com")
    except Exception as error:
        registrar_error(f"Simulación 2 correcta: error controlado por identificación vacía: {error}")

    # simulacion # 3
    try:
        gestor.registar_cliente("1003", "", "correo@email.com")
    except Exception as error:
        registrar_error(f"Simulación 3 correcta: error controlado por nombre vacío: {error}")


    # simulacion # 4
    try:
        gestor.registar_cliente("1004", "Laura", "correo_invalido")
    except Exception as error:
        registrar_error(f"Simulación 4 correcta: error controlado por correo inválido: {error}")

    # simulacion # 5
    try:
        sala = ReservarSala("Sala Ejecutiva", 50000)
        gestor.registrar_servicio(sala)
        registrar_evento("Simulación 5 correcta: servicio válido.")
    except Exception as error:
        registrar_error(f"Simulación 5 fallida: {error}")

    # simulacion # 6
    try:
        ReservaSala("Sala inválida", -10000)
    except Exception as error:
        registrar_error(f"Simulación 6 correcta: error controlado por precio negativo: {error}")

    # simulacion # 7
    try:
        equipo = AlquilerEquipo("Video Beam", 25000)
        gestor.registar_servicio(equipo)
        reserva = gestor.crear_reserva(cliente_1, equipo, 2)
        registrar_evento(f"Simulación 7 correcta: reserva creada: {reserva.mostrar_informacion()}")
    except Exception as error:
        registrar_error(f"Simulación 7 fallida: {error}")

    # simulacion # 8
    try:
        asesoria = AsesoriaEspecializada("Asesoría Python", 90000)
        gestor.registar_servicio(asesoria)
        gestor.crear_reserva(cliente_1, asesoria, 0)
    except Exception as error:
        registrar_error(f"Simulación 8 correcta: error controlado por duración inválida: {error}")

    # simulacion # 9
    try:
        sala_no_disponible = ReservarSala("Sala Ocupada", 60000)
        sala_no_disponible.disponible = False
        gestor.crear_reserva(cliente_1, sala_no_disponible, 2)
    except Exception as error:
        registrar_error(f"Simulación 9 correcta: error controlado por servicio no disponible: {error}")

    # simulacion # 10
    try:
        sala_final = ReservarSala("Sala Final", 70000)
        reserva_final = gestor.crear_reserva(cliente_1, sala_final, 1)
        reserva_final.cancelar()
        reserva_final.confirmar()
    except Exception as error:
        registrar_error(f"Simulación 10 correcta: error controlado al confirmar reserva cancelada: {error}")


if __name__ == "__main__":
    ejecutar_simulaciones()