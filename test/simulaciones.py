from sistema.gestor_sistema import GestorSistema
from clases.cliente import Cliente
from clases.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from clases.reserva import Reserva

def ejecutar_simulaciones()-> list[str]:
    resultados : list[str] = []
    gestor : GestorSistema = GestorSistema()

    # simulacion # 1
    try:
        cliente : Cliente = gestor.registar_cliente("1001", "Ana Pérez", "ana@email.com")
        resultados.append("Simulación 1 correcta: cliente válido.")
        resultados.append(cliente.mostrar_informacion())
    except Exception as error:
        resultados.append(f"Simulación 1 fallida: {error}")


    # Simulación 2: cliente sin identificación
    try:
        cliente: Cliente = gestor.registrar_cliente("", "Carlos Ruiz", "carlos@email.com")
        resultados.append("Simulación 2 fallida: se creó cliente sin identificación.")
        resultados.append(cliente.mostrar_informacion())
    except Exception as error:
        resultados.append(f"Simulación 2 correcta: cliente sin identificación rechazado: {error}")

    # Simulación 3: cliente sin nombre
    try:
        cliente: Cliente = gestor.registrar_cliente("1003", "", "laura@email.com")
        resultados.append("Simulación 3 fallida: se creó cliente sin nombre.")
        resultados.append(cliente.mostrar_informacion())
    except Exception as error:
        resultados.append(f"Simulación 3 correcta: cliente sin nombre rechazado: {error}")

    # Simulación 4: cliente con correo inválido
    try:
        cliente: Cliente = gestor.registrar_cliente("1004", "Laura Gómez", "correo_invalido")
        resultados.append("Simulación 4 fallida: se creó cliente con correo inválido.")
        resultados.append(cliente.mostrar_informacion())
    except Exception as error:
        resultados.append(f"Simulación 4 correcta: correo inválido rechazado: {error}")

    # Simulación 5: servicio válido
    try:
        servicio: ReservaSala = ReservaSala("Sala Ejecutiva", 50000)
        gestor.registrar_servicio(servicio)
        resultados.append("Simulación 5 correcta: servicio válido creado.")
        resultados.append(servicio.describir())
    except Exception as error:
        resultados.append(f"Simulación 5 fallida: {error}")

    # Simulación 6: servicio con precio negativo
    try:
        servicio: ReservaSala = ReservaSala("Sala inválida", -10000)
        gestor.registrar_servicio(servicio)
        resultados.append("Simulación 6 fallida: se creó servicio con precio negativo.")
    except Exception as error:
        resultados.append(f"Simulación 6 correcta: servicio con precio negativo rechazado: {error}")

    # Simulación 7: reserva válida
    try:
        cliente: Cliente = gestor.registrar_cliente("2001", "Andrés Pérez", "andres@email.com")
        servicio: AlquilerEquipo = AlquilerEquipo("Video Beam", 25000)
        gestor.registrar_servicio(servicio)

        reserva: Reserva = gestor.crear_reserva(cliente, servicio, 2)
        reserva.confirmar()

        resultados.append("Simulación 7 correcta: reserva válida creada y confirmada.")
        resultados.append(reserva.mostrar_informacion())
    except Exception as error:
        resultados.append(f"Simulación 7 fallida: {error}")

    # Simulación 8: reserva con duración cero
    try:
        cliente: Cliente = gestor.registrar_cliente("2002", "María López", "maria@email.com")
        servicio: AsesoriaEspecializada = AsesoriaEspecializada("Asesoría Python", 90000)
        gestor.registrar_servicio(servicio)

        reserva: Reserva = gestor.crear_reserva(cliente, servicio, 0)
        resultados.append("Simulación 8 fallida: se creó reserva con duración cero.")
        resultados.append(reserva.mostrar_informacion())
    except Exception as error:
        resultados.append(f"Simulación 8 correcta: reserva con duración cero rechazada: {error}")

    # Simulación 9: reserva con servicio no disponible
    try:
        cliente: Cliente = gestor.registrar_cliente("2003", "Camila Torres", "camila@email.com")
        servicio: ReservaSala = ReservaSala("Sala Ocupada", 60000)
        servicio.disponible = False

        reserva: Reserva = gestor.crear_reserva(cliente, servicio, 2)
        resultados.append("Simulación 9 fallida: se creó reserva con servicio no disponible.")
        resultados.append(reserva.mostrar_informacion())
    except Exception as error:
        resultados.append(f"Simulación 9 correcta: servicio no disponible rechazado: {error}")

    # Simulación 10: confirmar reserva cancelada
    try:
        cliente: Cliente = gestor.registrar_cliente("2004", "Sofía Ramírez", "sofia@email.com")
        servicio: ReservaSala = ReservaSala("Sala Final", 70000)
        gestor.registrar_servicio(servicio)

        reserva: Reserva = gestor.crear_reserva(cliente, servicio, 1)
        reserva.cancelar()
        reserva.confirmar()

        resultados.append("Simulación 10 fallida: se confirmó una reserva cancelada.")
    except Exception as error:
        resultados.append(f"Simulación 10 correcta: no se pudo confirmar reserva cancelada: {error}")

    return resultados


if __name__ == "__main__":
    mensajes: list[str] = ejecutar_simulaciones()

    for mensaje in mensajes:
        print(mensaje)