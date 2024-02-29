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

    def agregar_empleado(self, empleado):
        if isinstance(empleado, Empleado):
            self.empleados.append(empleado)

    def establecer_configuracion(self, configuracion):
        if isinstance(configuracion, ConfiguracionRestaurante):
            self.configuracion = configuracion

    def establecer_calendario_reservas(self, calendario):
        if isinstance(calendario, CalendarioReservas):
            self.calendario_reservas = calendario
