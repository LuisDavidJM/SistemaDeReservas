from Empleado import Empleado
from ConfiguracionRestaurante import ConfiguracionRestaurante

class Propietario(Empleado):
    def __init__(self, nombre, identificacion, correoElectronico, telefono, accesoTotal, emailNotificaciones):
        super().__init__(nombre, identificacion, correoElectronico, telefono)
        self.accesoTotal = accesoTotal
        self.emailNotificaciones = emailNotificaciones

    # Solicita y devuelve la configuración actual del restaurante.
    def solicitarConfActual(self, ConfiguracionRestaurante):
        return f"Configuración actual del restaurante: Capacidad máxima: {ConfiguracionRestaurante.capacidadMaxima}, Horarios de operación: {ConfiguracionRestaurante.horariosOperacion}"

    # Decide y aplica cambios a la configuración del restaurante si se tiene acceso total.
    def decidirCambios(self, ConfiguracionRestaurante, nuevaCapacidadMaxima=None, nuevosHorariosOperacion=None):
        if self.accesoTotal:
            if nuevaCapacidadMaxima is not None:
                ConfiguracionRestaurante.capacidadMaxima = nuevaCapacidadMaxima
            if nuevosHorariosOperacion is not None:
                ConfiguracionRestaurante.horariosOperacion = nuevosHorariosOperacion
            return "Se han aplicado los cambios en la configuración del restaurante."
            
        else:
            return "No tiene acceso para decidir cambios en la configuración del restaurante."
