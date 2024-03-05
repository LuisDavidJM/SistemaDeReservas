from Reserva import Reserva

class Cliente:
    def __init__(self, nombre, correoElectronico, telefono, idCliente):
        self.nombre = nombre
        self.correoElectronico = correoElectronico
        self.telefono = telefono
        self.idCliente = idCliente
        self.reservas = []  # Esta será una lista de instancias de Reserva

    # Agrega una reserva a la lista de reservas del cliente.
    def agregarReserva(self, fecha, hora, numeroDePersonas, idReserva):
        nuevaReserva = Reserva(fecha, hora, numeroDePersonas, idReserva)
        self.reservas.append(nuevaReserva)

    # Simula el proceso de solicitar una reserva, devolviendo un mensaje que indica la solicitud.
    def solicitarReserva(self, fecha, hora, numeroDePersonas):
        return f"Reserva solicitada para {numeroDePersonas} personas el {fecha} a las {hora}."

    # Devuelve una cadena con la información básica del cliente.
    def pedirInformacion(self):
        return f"Información del Cliente: {self.nombre}, Email: {self.correoElectronico}, Teléfono: {self.telefono}"
        
