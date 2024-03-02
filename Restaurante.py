from ConfiguracionRestaurante import ConfiguracionRestaurante
from Empleado import Empleado
from CalendarioReservas import CalendarioReservas

class Restaurante:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.empleados = []  # Agregación de Empleados
        self.configuracion = None  # Agregación de ConfiguracionRestaurante
        self.calendario_reservas = None  # Agregación de CalendarioReservas

    # Añade un empleado a la lista de empleados si el objeto pasado es una instancia de Empleado.
    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            self.empleados.append(empleado)

    # Establece la configuración del restaurante si el objeto pasado es una instancia de ConfiguracionRestaurante.
    def establecer_configuracion(self, configuracion):
        if isinstance(configuracion, ConfiguracionRestaurante):
            self.configuracion = configuracion

    # Establece el calendario de reservas si el objeto pasado es una instancia de CalendarioReservas.
    def establecer_calendario_reservas(self, calendario):
        if isinstance(calendario, CalendarioReservas):
            self.calendario_reservas = calendario
