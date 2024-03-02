from Reserva import Reserva

class Cliente:
    def __init__(self, nombre, correo_electronico, telefono, id_cliente):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.id_cliente = id_cliente
        self.reservas = []  # Esta será una lista de instancias de Reserva

    # Agrega una reserva a la lista de reservas del cliente.
    def agregar_reserva(self, fecha, hora, numero_personas, id_reserva):
        nueva_reserva = Reserva(fecha, hora, numero_personas, id_reserva)
        self.reservas.append(nueva_reserva)

    # Simula el proceso de solicitar una reserva, devolviendo un mensaje que indica la solicitud.
    def solicitar_reserva(self, fecha, hora, numero_personas):
        return f"Reserva solicitada para {numero_personas} personas el {fecha} a las {hora}."

    # Devuelve una cadena con la información básica del cliente.
    def pedir_informacion(self):
        return f"Información del Cliente: {self.nombre}, Email: {self.correo_electronico}, Teléfono: {self.telefono}"
        
