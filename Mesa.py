class Mesa:
    def __init__(self, numero_mesa, capacidad, ubicacion, disponible=True):
        self.numero_mesa = numero_mesa
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.disponible = disponible

    # Informa sobre la disponibilidad de la mesa, marcándola como no disponible.
    def informar_disponibilidad(self):
        self.disponible = False
        return f"La mesa {self.numero_mesa} está disponible."

    # Marca la mesa como no disponible y devuelve un mensaje indicando este estado.
    def informar_no_disponibilidad(self):
        self.disponible = False
        return f"La mesa {self.numero_mesa} no está disponible."

    # Proporciona información sobre la disposición de la mesa, incluyendo su ubicación y capacidad.
    def proveer_disposicion(self):
        return f"Mesa {self.numero_mesa}: Ubicación: {self.ubicacion}, Capacidad: {self.capacidad} personas."

    # Aplica cambios a la capacidad y/o ubicación de la mesa según los parámetros proporcionados.
    def aplicar_nuevos_cambios(self, nueva_capacidad=None, nueva_ubicacion=None):
        if nueva_capacidad:
            self.capacidad = nueva_capacidad
        if nueva_ubicacion:
            self.ubicacion = nueva_ubicacion
        return f"Se han aplicado cambios a la mesa {self.numero_mesa}: Nueva capacidad: {self.capacidad}, Nueva ubicación: {self.ubicacion}."
