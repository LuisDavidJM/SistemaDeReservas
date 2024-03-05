from Mesa import Mesa

class Reserva:
    def __init__(self, fecha, hora, numeroDePersonas, idReserva):
        self.fecha = fecha
        self.hora = hora
        self.numeroDePersonas = numeroDePersonas
        self.idReserva = idReserva
        self.mesas = [] # Lista para almacenar instancias de Mesa

    # Agrega una nueva mesa a la reserva, creando una instancia de Mesa y añadiéndola a la lista de mesas.
    def agregarMesa(self, numeroMesa, capacidad, ubicacion, disponible):
        nuevaMesa = Mesa(numeroMesa, capacidad, ubicacion, disponible)
        self.mesas.append(nuevaMesa)

    # Proporciona detalles de la reserva, imprimiendo información sobre la reserva y las mesas asignadas.
    def proveerDetalles(self):
        print(f"Reserva ID: {self.idReserva} para {self.numeroDePersonas} personas el {self.fecha} a las {self.hora}.")
        print("Mesas asignadas:")
        for mesa in self.mesas:
            disponibilidad = "disponible" if mesa.disponible else "no disponible"
            print(f"  Mesa {mesa.numeroMesa}: Capacidad para {mesa.capacidad} personas, Ubicación: {mesa.ubicacion}, Actualmente {disponibilidad}.")

    # Marca todas las mesas asignadas a la reserva como disponibles, indicando que el cliente no se presentó.
    def clienteNoPresente(self):
        for mesa in self.mesas:
            mesa.disponible = True
        return f"Reserva {self.idReserva} marcada como no cumplida. Todas las mesas han sido liberadas y están disponibles."
