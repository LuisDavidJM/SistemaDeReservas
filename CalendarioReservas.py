from Reserva import Reserva

class CalendarioReservas:
    def __init__(self, fechaInicio, fechaFin, idCalendario):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.idCalendario = idCalendario
        self.reservas = []  # Esta será una lista de instancias de Reserva

    # Agrega una nueva reserva al calendario, creando y almacenando una instancia de Reserva.
    def agregarReserva(self, fecha, hora, numeroDePersonas, idReserva):
        nueva_reserva = Reserva(fecha, hora, numeroDePersonas, idReserva)
        self.reservas.append(nueva_reserva)

    # Busca una reserva por su ID y devuelve los detalles de la misma si es encontrada.
    def encontrarDetalles(self, idReserva):
        for reserva in self.reservas:
            if reserva.idReserva == idReserva:
                return f"Reserva ID: {reserva.idReserva}, Fecha: {reserva.fecha}, Hora: {reserva.hora}, Numero de Personas: {reserva.numeroDePersonas}"
        return "Reserva no encontrada."
