from Empleado import Empleado
from ConfiguracionRestaurante import ConfiguracionRestaurante

class Propietario(Empleado):
    def __init__(self, nombre, identificacion, correo_electronico, telefono, acceso_total, email_notificaciones):
        super().__init__(nombre, identificacion, correo_electronico, telefono)
        self.acceso_total = acceso_total
        self.email_notificaciones = email_notificaciones

    # Solicita y devuelve la configuración actual del restaurante.
    def solicitar_confi_actual(self, configuracion_restaurante):
        return f"Configuración actual del restaurante: Capacidad máxima: {configuracion_restaurante.capacidad_maxima}, Horarios de operación: {configuracion_restaurante.horarios_operacion}"

    # Decide y aplica cambios a la configuración del restaurante si se tiene acceso total.
    def decidir_cambios(self, configuracion_restaurante, nueva_capacidad_maxima=None, nuevos_horarios_operacion=None):
        if self.acceso_total:
            if nueva_capacidad_maxima is not None:
                configuracion_restaurante.capacidad_maxima = nueva_capacidad_maxima
            if nuevos_horarios_operacion is not None:
                configuracion_restaurante.horarios_operacion = nuevos_horarios_operacion
            return "Se han aplicado los cambios en la configuración del restaurante."
            
        else:
            return "No tiene acceso para decidir cambios en la configuración del restaurante."
