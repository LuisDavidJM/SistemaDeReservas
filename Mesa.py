class Mesa:
    def __init__(self, numero_mesa, capacidad, ubicacion, disponible=True):
        self.numero_mesa = numero_mesa
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.disponible = disponible

    def informar_disponibilidad(self):
        # Imprime el estado de disponibilidad de la mesa
        if self.disponible:
            print(f"La mesa {self.numero_mesa} está disponible.")
        else:
            print(f"La mesa {self.numero_mesa} no está disponible.")

    def informar_no_disponibilidad(self):
        # Marca la mesa como no disponible
        self.disponible = False
        print(f"La mesa {self.numero_mesa} ha sido marcada como no disponible.")

    def proveer_disposicion(self):
        # Imprime la disposición de la mesa incluyendo ubicación y capacidad
        print(f"Mesa {self.numero_mesa}: Ubicación: {self.ubicacion}, Capacidad: {self.capacidad} personas.")

    def aplicar_nuevos_cambios(self, nueva_capacidad=None, nueva_ubicacion=None):
        # Aplica cambios en la capacidad y/o ubicación de la mesa
        if nueva_capacidad:
            self.capacidad = nueva_capacidad
        if nueva_ubicacion:
            self.ubicacion = nueva_ubicacion
        print(f"Se han aplicado cambios a la mesa {self.numero_mesa}: Nueva capacidad: {self.capacidad}, Nueva ubicación: {self.ubicacion}.")
