from Reserva import Reserva

class CalendarioReservas:
    def __init__(self, fecha_inicio, fecha_fin, id_calendario):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.id_calendario = id_calendario
        self.reservas = []  # Esta será una lista de instancias de Reserva

    # Agrega una nueva reserva al calendario, creando y almacenando una instancia de Reserva.
    def agregar_reserva(self, fecha, hora, numero_personas, id_reserva):
        nueva_reserva = Reserva(fecha, hora, numero_personas, id_reserva)
        self.reservas.append(nueva_reserva)

    # Busca una reserva por su ID y devuelve los detalles de la misma si es encontrada.
    def encontrar_detalles(self, id_reserva):
        for reserva in self.reservas:
            if reserva.id_reserva == id_reserva:
                return f"Reserva ID: {reserva.id_reserva}, Fecha: {reserva.fecha}, Hora: {reserva.hora}, Numero de Personas: {reserva.numero_personas}"
        return "Reserva no encontrada."
