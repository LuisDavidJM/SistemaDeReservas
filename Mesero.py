from Empleado import Empleado
from CalendarioReservas import CalendarioReservas

class Mesero(Empleado):
    def __init__(self, nombre, identificacion, correoElectronico, telefono, turnos, seccion):
        super().__init__(nombre, identificacion, correoElectronico, telefono)
        self.turnos = turnos
        self.seccion = seccion

    # Intenta hacer una reserva en el calendario de reservas del restaurante.
    def hacerReserva(self, calendarioReservas, fecha, hora, numeroDePersonas, idReserva):
        if isinstance(calendarioReservas, CalendarioReservas):
            calendarioReservas.agregarReserva(fecha, hora, numeroDePersonas, idReserva)
            return f"Reserva creada con éxito. ID de reserva: {idReserva}."
        else:
            return "El sistema de reservas no está disponible. Por favor, intente de nuevo más tarde."

    # Informa al cliente que su reserva ha sido confirmada.
    def informarReservaConfirmada(self, idReserva):
        return f"La reserva con ID {idReserva} ha sido confirmada. Por favor, presente esta información al llegar."

    # Informa al cliente que no hay disponibilidad para la fecha y hora solicitadas.
    def informarReservaNoDisponible(self, fecha, hora):
        return f"Lo sentimos, no hay disponibilidad para el {fecha} a las {hora}. Por favor, elija otra fecha u hora."

    # Marca el servicio como completado para una reserva específica.
    def finalizarServicio(self, idReserva):
        return f"Servicio completado para la reserva con ID {idReserva}. Esperamos que haya disfrutado su estancia."

    # Informa sobre la necesidad de cancelar una reserva.
    def cancelarServicio(self, idReserva):
        return f"Se ha solicitado la cancelación de la reserva con ID {idReserva}. Por favor, contacte a la administración para proceder."
