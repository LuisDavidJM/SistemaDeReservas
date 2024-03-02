from Mesa import Mesa

class Reserva:
    def __init__(self, fecha, hora, numero_personas, id_reserva):
        self.fecha = fecha
        self.hora = hora
        self.numero_personas = numero_personas
        self.id_reserva = id_reserva
        self.mesas = [] # Lista para almacenar instancias de Mesa

    # Agrega una nueva mesa a la reserva, creando una instancia de Mesa y añadiéndola a la lista de mesas.
    def agregar_mesa(self, numero_mesa, capacidad, ubicacion, disponible):
        nueva_mesa = Mesa(numero_mesa, capacidad, ubicacion, disponible)
        self.mesas.append(nueva_mesa)

    # Proporciona detalles de la reserva, imprimiendo información sobre la reserva y las mesas asignadas.
    def proveer_detalles(self):
        print(f"Reserva ID: {self.id_reserva} para {self.numero_personas} personas el {self.fecha} a las {self.hora}.")
        print("Mesas asignadas:")
        for mesa in self.mesas:
            disponibilidad = "disponible" if mesa.disponible else "no disponible"
            print(f"  Mesa {mesa.numero_mesa}: Capacidad para {mesa.capacidad} personas, Ubicación: {mesa.ubicacion}, Actualmente {disponibilidad}.")

    # Marca todas las mesas asignadas a la reserva como disponibles, indicando que el cliente no se presentó.
    def cliente_no_presente(self):
        for mesa in self.mesas:
            mesa.disponible = True
        return f"Reserva {self.id_reserva} marcada como no cumplida. Todas las mesas han sido liberadas y están disponibles."
