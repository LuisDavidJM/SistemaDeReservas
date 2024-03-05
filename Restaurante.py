from ConfiguracionRestaurante import ConfiguracionRestaurante
from Empleado import Empleado
from CalendarioReservas import CalendarioReservas

class Restaurante:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.Empleado = []  # Agregación de Empleados
        self.ConfiguracionRestaurante = None  # Agregación de ConfiguracionRestaurante
        self.CalendarioReservas = None  # Agregación de CalendarioReservas

    # Añade un empleado a la lista de empleados si el objeto pasado es una instancia de Empleado.
    def agregarEmpleado(self, empleado):
        if isinstance(empleado, Empleado):
            self.Empleado.append(empleado)

    # Establece la configuración del restaurante si el objeto pasado es una instancia de ConfiguracionRestaurante.
    def establecerConfiguracion(self, configuracion):
        if isinstance(configuracion, ConfiguracionRestaurante):
            self.ConfiguracionRestaurante = configuracion

    # Establece el calendario de reservas si el objeto pasado es una instancia de CalendarioReservas.
    def establecerCalendarioReservas(self, calendario):
        if isinstance(calendario, CalendarioReservas):
            self.CalendarioReservas = calendario
