from Mesa import Mesa

class ConfiguracionRestaurante:
    def __init__(self, capacidadMaxima, horariosOperacion, idConfiguracion):
        self.capacidadMaxima = capacidadMaxima
        self.horariosOperacion = horariosOperacion
        self.idConfiguracion = idConfiguracion
        self.mesas = []  # Agregación de Mesa

    # Agrega una mesa a la configuración del restaurante si el objeto es una instancia de Mesa.
    def agregarMesa(self, mesa):
        if isinstance(mesa, Mesa):
            self.mesas.append(mesa)

    # Verifica la disponibilidad de las mesas, retornando True si hay al menos una disponible.
    def verificarDisponibilidad(self):
        for mesa in self.mesas:
            if mesa.disponible and mesa.numeroMesa < 3:
                return True
        return False

    # Confirma la reserva de una mesa específica, marcándola como no disponible.
    def reservaConfirmada(self, numeroMesa):
        for mesa in self.mesas:
            if mesa.numeroMesa == numeroMesa:
                mesa.disponible = False
                return f"Reserva confirmada para la mesa {numeroMesa}."
        return "Mesa no encontrada."

    # Marca una mesa específica como no disponible sin asociarla a una reserva específica.
    def reservaNoDisponible(self, numeroMesa):
        for mesa in self.mesas:
            if mesa.numeroMesa == numeroMesa:
                mesa.disponible = False
                return f"Mesa {numeroMesa} marcada como no disponible."
        return "Mesa no encontrada."

    # Placeholder para un método que buscaría una reserva por ID.
    def buscarReserva(self, id_reserva):
        return f"Buscando reserva con ID: {id_reserva}"

    # Imprime la información actual sobre la configuración del restaurante y el estado de las mesas.
    def mostrarInformacion(self):
        print(f"Configuración del Restaurante ID: {self.idConfiguracion}")
        print(f"Capacidad máxima: {self.capacidadMaxima}")
        print(f"Horarios de operación: {self.horariosOperacion}")
        for mesa in self.mesas:
            estado = "Disponible" if mesa.disponible else "No disponible"
            print(f"Mesa {mesa.numeroMesa}, Capacidad: {mesa.capacidad}, Ubicación: {mesa.ubicacion}, Estado: {estado}")

    # Muestra la disposición actual de las mesas en el restaurante.
    def consultarDisposicion(self):
        for mesa in self.mesas:
            estado = "Disponible" if mesa.disponible else "No disponible"
            return f"Mesa {mesa.numeroMesa} está {estado}."

    # Notifica sobre cambios específicos en la configuración del restaurante.
    def notificarCambios(self, mensaje):
        return f"Notificación: {mensaje}"

    # Actualiza la capacidad máxima del restaurante a un nuevo valor.
    def actualizarTiempoReal(self, nuevaCapacidad):
        self.capacidadMaxima = nuevaCapacidad
        return f"Capacidad máxima actualizada a {nuevaCapacidad}."
