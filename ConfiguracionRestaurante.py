from Mesa import Mesa

class ConfiguracionRestaurante:
    def __init__(self, capacidad_maxima, horarios_operacion, id_configuracion):
        self.capacidad_maxima = capacidad_maxima
        self.horarios_operacion = horarios_operacion
        self.id_configuracion = id_configuracion
        self.mesas = []  # Agregación de Mesa

    # Agrega una mesa a la configuración del restaurante si el objeto es una instancia de Mesa.
    def agregar_mesa(self, mesa):
        if isinstance(mesa, Mesa):
            self.mesas.append(mesa)

    # Verifica la disponibilidad de las mesas, retornando True si hay al menos una disponible.
    def verificar_disponibilidad(self):
        for mesa in self.mesas:
            if mesa.disponible and mesa.numero_mesa < 3:
                return True
        return False

    # Confirma la reserva de una mesa específica, marcándola como no disponible.
    def reserva_confirmada(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero_mesa == numero_mesa:
                mesa.disponible = False
                return f"Reserva confirmada para la mesa {numero_mesa}."
        return "Mesa no encontrada."

    # Marca una mesa específica como no disponible sin asociarla a una reserva específica.
    def reserva_no_disponible(self, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero_mesa == numero_mesa:
                mesa.disponible = False
                return f"Mesa {numero_mesa} marcada como no disponible."
        return "Mesa no encontrada."

    # Placeholder para un método que buscaría una reserva por ID.
    def buscar_reserva(self, id_reserva):
        return f"Buscando reserva con ID: {id_reserva}"

    # Imprime la información actual sobre la configuración del restaurante y el estado de las mesas.
    def mostrar_informacion(self):
        print(f"Configuración del Restaurante ID: {self.id_configuracion}")
        print(f"Capacidad máxima: {self.capacidad_maxima}")
        print(f"Horarios de operación: {self.horarios_operacion}")
        for mesa in self.mesas:
            estado = "Disponible" if mesa.disponible else "No disponible"
            print(f"Mesa {mesa.numero_mesa}, Capacidad: {mesa.capacidad}, Ubicación: {mesa.ubicacion}, Estado: {estado}")

    # Muestra la disposición actual de las mesas en el restaurante.
    def consultar_disposicion(self):
        for mesa in self.mesas:
            estado = "Disponible" if mesa.disponible else "No disponible"
            return f"Mesa {mesa.numero_mesa} está {estado}."

    # Notifica sobre cambios específicos en la configuración del restaurante.
    def notificar_cambios(self, mensaje):
        return f"Notificación: {mensaje}"

    # Actualiza la capacidad máxima del restaurante a un nuevo valor.
    def actualizar_tiempo_real(self, nueva_capacidad):
        self.capacidad_maxima = nueva_capacidad
        return f"Capacidad máxima actualizada a {nueva_capacidad}."
