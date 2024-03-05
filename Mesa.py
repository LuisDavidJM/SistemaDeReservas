class Mesa:
    def __init__(self, numeroMesa, capacidad, ubicacion, disponible=True):
        self.numeroMesa = numeroMesa
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.disponible = disponible

    # Informa sobre la disponibilidad de la mesa, marcándola como no disponible.
    def informarDisponibilidad(self):
        self.disponible = False
        return f"La mesa {self.numeroMesa} está disponible."

    # Marca la mesa como no disponible y devuelve un mensaje indicando este estado.
    def informarNoDisponibilidad(self):
        self.disponible = False
        return f"La mesa {self.numeroMesa} no está disponible."

    # Proporciona información sobre la disposición de la mesa, incluyendo su ubicación y capacidad.
    def proveerDisposicion(self):
        return f"Mesa {self.numeroMesa}: Ubicación: {self.ubicacion}, Capacidad: {self.capacidad} personas."

    # Aplica cambios a la capacidad y/o ubicación de la mesa según los parámetros proporcionados.
    def aplicarNuevosCambios(self, nuevaCapacidad=None, nuevaUbicacion=None):
        if nuevaCapacidad:
            self.capacidad = nuevaCapacidad
        if nuevaUbicacion:
            self.ubicacion = nuevaUbicacion
        return f"Se han aplicado cambios a la mesa {self.numeroMesa}: Nueva capacidad: {self.capacidad}, Nueva ubicación: {self.ubicacion}."
