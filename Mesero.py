from Empleado import Empleado
from CalendarioReservas import CalendarioReservas

class Mesero(Empleado):
    def __init__(self, nombre, identificacion, correo_electronico, telefono, turnos, seccion):
        super().__init__(nombre, identificacion, correo_electronico, telefono)
        self.turnos = turnos
        self.seccion = seccion

    def hacer_reserva(self, calendario_reservas, fecha, hora, numero_personas, id_reserva):
        # Asumiendo que calendario_reservas es una instancia de CalendarioReservas
        if isinstance(calendario_reservas, CalendarioReservas):
            calendario_reservas.agregar_reserva(fecha, hora, numero_personas, id_reserva)
            print(f"Reserva creada con éxito. ID de reserva: {id_reserva}.")
        else:
            print("El sistema de reservas no está disponible. Por favor, intente de nuevo más tarde.")

    def informar_reserva_confirmada(self, id_reserva):
        # Informa al cliente que su reserva ha sido confirmada
        print(f"La reserva con ID {id_reserva} ha sido confirmada. Por favor, presente esta información al llegar.")

    def informar_reserva_no_disponible(self, fecha, hora):
        # Informa al cliente que no hay disponibilidad para la fecha y hora solicitadas
        print(f"Lo sentimos, no hay disponibilidad para el {fecha} a las {hora}. Por favor, elija otra fecha u hora.")

    def finalizar_servicio(self, id_reserva):
        # Marca el servicio como completado para una reserva específica
        print(f"Servicio completado para la reserva con ID {id_reserva}. Esperamos que haya disfrutado su estancia.")

    def cancelar_servicio(self, id_reserva):
        # Informa sobre la necesidad de cancelar una reserva
        print(f"Se ha solicitado la cancelación de la reserva con ID {id_reserva}. Por favor, contacte a la administración para proceder.")
