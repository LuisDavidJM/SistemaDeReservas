from Empleado import Empleado
from ConfiguracionRestaurante import ConfiguracionRestaurante

class Propietario(Empleado):
    def __init__(self, nombre, identificacion, correo_electronico, telefono, acceso_total, email_notificaciones):
        super().__init__(nombre, identificacion, correo_electronico, telefono)
        self.acceso_total = acceso_total
        self.email_notificaciones = email_notificaciones

    def solicitar_confi_actual(self, configuracion_restaurante):
        # Imprime la configuración actual del restaurante directamente
        print(f"Configuración actual del restaurante: Capacidad máxima: {configuracion_restaurante.capacidad_maxima}, Horarios de operación: {configuracion_restaurante.horarios_operacion}")

    def decidir_cambios(self, configuracion_restaurante, nueva_capacidad_maxima=None, nuevos_horarios_operacion=None):
        # Aplica cambios en la configuración del restaurante directamente
        if self.acceso_total:
            if nueva_capacidad_maxima is not None:
                configuracion_restaurante.capacidad_maxima = nueva_capacidad_maxima
            if nuevos_horarios_operacion is not None:
                configuracion_restaurante.horarios_operacion = nuevos_horarios_operacion
            print("Se han aplicado los cambios en la configuración del restaurante.")
            
            if self.email_notificaciones:
                print(f"Enviando notificación de cambios a {self.correo_electronico}...")
        else:
            print("No tiene acceso para decidir cambios en la configuración del restaurante.")
