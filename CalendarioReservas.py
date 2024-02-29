from Reserva import Reserva

class CalendarioReservas:
    def __init__(self, fecha_inicio, fecha_fin, id_calendario):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.id_calendario = id_calendario
        self.reservas = []  # Esta será una lista de instancias de Reserva

    def agregar_reserva(self, fecha, hora, numero_personas, id_reserva):
        # Crear una nueva instancia de Reserva y agregarla a la lista de reservas
        nueva_reserva = Reserva(fecha, hora, numero_personas, id_reserva)
        self.reservas.append(nueva_reserva)

    def encontrar_detalles(self, id_reserva):
        # Busca en la lista de reservas por ID y devuelve los detalles si la encuentra
        for reserva in self.reservas:
            if reserva.id_reserva == id_reserva:
                return f"Reserva ID: {reserva.id_reserva}, Fecha: {reserva.fecha}, Hora: {reserva.hora}, Numero de Personas: {reserva.numero_personas}"
        return "Reserva no encontrada."
