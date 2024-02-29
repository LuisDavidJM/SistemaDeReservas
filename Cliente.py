from Reserva import Reserva

class Cliente:
    def __init__(self, nombre, correo_electronico, telefono, id_cliente):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.id_cliente = id_cliente
        self.reservas = []  # Esta será una lista de instancias de Reserva

    def agregar_reserva(self, fecha, hora, numero_personas, id_reserva):
        # Crear una nueva instancia de Reserva y agregarla a la lista de reservas
        nueva_reserva = Reserva(fecha, hora, numero_personas, id_reserva)
        self.reservas.append(nueva_reserva)

    def solicitar_reserva(self, fecha, hora, numero_personas):
        # Simula la solicitud de una nueva reserva
        id_reserva = len(self.reservas) + 1  # Genera un ID simple para la demostración
        self.agregar_reserva(fecha, hora, numero_personas, id_reserva)
        print(f"Reserva solicitada para {numero_personas} personas el {fecha} a las {hora}. ID de reserva: {id_reserva}")

    def pedir_informacion(self):
        # Imprime la información del cliente y todas sus reservas
        print(f"Información del Cliente: {self.nombre}, Email: {self.correo_electronico}, Teléfono: {self.telefono}")
        if self.reservas:
            print("Reservas:")
            for reserva in self.reservas:
                print(f"  ID: {reserva.id_reserva}, Fecha: {reserva.fecha}, Hora: {reserva.hora}, Número de Personas: {reserva.numero_personas}")
        else:
            print("No hay reservas actualmente.")
