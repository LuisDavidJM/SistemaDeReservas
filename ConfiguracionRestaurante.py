from Mesa import Mesa

class ConfiguracionRestaurante:
    def __init__(self, capacidad_maxima, horarios_operacion, id_configuracion):
        self.capacidad_maxima = capacidad_maxima
        self.horarios_operacion = horarios_operacion
        self.id_configuracion = id_configuracion
        self.mesas = []  # Agregación de Mesa

    def agregar_mesa(self, mesa):
        if isinstance(mesa, Mesa):
            self.mesas.append(mesa)

    def verificar_disponibilidad(self):
        # Verifica si hay al menos una mesa disponible
        for mesa in self.mesas:
            if mesa.disponible:
                return True
        return False

    def reserva_confirmada(self, numero_mesa):
        # Busca la mesa por número y marca como no disponible si se encuentra
        for mesa in self.mesas:
            if mesa.numero_mesa == numero_mesa:
                mesa.disponible = False
                print(f"Reserva confirmada para la mesa {numero_mesa}.")
                return
        print("Mesa no encontrada.")

    def reserva_no_disponible(self, numero_mesa):
        # Marca una mesa como no disponible sin realizar una reserva
        for mesa in self.mesas:
            if mesa.numero_mesa == numero_mesa:
                mesa.disponible = False
                print(f"Mesa {numero_mesa} marcada como no disponible.")
                return
        print("Mesa no encontrada.")

    def buscar_reserva(self, id_reserva):
        # Este método es un placeholder, la lógica real dependería de cómo se almacenan las reservas
        print(f"Buscando reserva con ID: {id_reserva}")

    def mostrar_informacion(self):
        print(f"Configuración del Restaurante ID: {self.id_configuracion}")
        print(f"Capacidad máxima: {self.capacidad_maxima}")
        print(f"Horarios de operación: {self.horarios_operacion}")
        for mesa in self.mesas:
            estado = "Disponible" if mesa.disponible else "No disponible"
            print(f"Mesa {mesa.numero_mesa}, Capacidad: {mesa.capacidad}, Ubicación: {mesa.ubicacion}, Estado: {estado}")

    def consultar_disposicion(self):
        # Muestra la disposición de todas las mesas
        for mesa in self.mesas:
            estado = "Disponible" if mesa.disponible else "No disponible"
            print(f"Mesa {mesa.numero_mesa} está {estado}.")

    def notificar_cambios(self, mensaje):
        # Notifica sobre cambios en la configuración o estado de las mesas
        print(f"Notificación: {mensaje}")

    def actualizar_tiempo_real(self, nueva_capacidad):
        # Actualiza la capacidad máxima del restaurante
        self.capacidad_maxima = nueva_capacidad
        print(f"Capacidad máxima actualizada a {nueva_capacidad}.")
