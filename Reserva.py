from Mesa import Mesa

class Reserva:
    def __init__(self, fecha, hora, numero_personas, id_reserva):
        self.fecha = fecha
        self.hora = hora
        self.numero_personas = numero_personas
        self.id_reserva = id_reserva
        self.mesas = [] # Lista para almacenar instancias de Mesa

    def agregar_mesa(self, numero_mesa, capacidad, ubicacion, disponible):
        # Crear una nueva instancia de Mesa y agregarla a la lista de mesas
        nueva_mesa = Mesa(numero_mesa, capacidad, ubicacion, disponible)
        self.mesas.append(nueva_mesa)

    def proveer_detalles(self):
        # Imprime los detalles de la reserva incluyendo las mesas asignadas
        print(f"Reserva ID: {self.id_reserva} para {self.numero_personas} personas el {self.fecha} a las {self.hora}.")
        print("Mesas asignadas:")
        for mesa in self.mesas:
            disponibilidad = "disponible" if mesa.disponible else "no disponible"
            print(f"  Mesa {mesa.numero_mesa}: Capacidad para {mesa.capacidad} personas, Ubicación: {mesa.ubicacion}, Actualmente {disponibilidad}.")

    def cliente_no_presente(self):
        # Marca todas las mesas asignadas a la reserva como disponibles nuevamente
        for mesa in self.mesas:
            mesa.disponible = True
        print(f"Reserva {self.id_reserva} marcada como no cumplida. Todas las mesas han sido liberadas y están disponibles.")
