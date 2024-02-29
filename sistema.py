from Restaurante import Restaurante
from Empleado import Empleado
from Mesero import Mesero
from Propietario import Propietario
from Cliente import Cliente
from Reserva import Reserva
from Mesa import Mesa
from CalendarioReservas import CalendarioReservas
from ConfiguracionRestaurante import ConfiguracionRestaurante

def main():
    # Inicialización de entidades
    restaurante = Restaurante("El Buen Sabor", "Calle Principal #123")
    propietario = Propietario("Juan Pérez", "ID001", "juan@elbuensor.com", "555-1000", True, True)
    mesero = Mesero("Ana Gómez", "ID002", "ana@elbuensor.com", "555-2000", ["Mañana"], "Sección A")
    cliente = Cliente("Carlos López", "carlos@ejemplo.com", "555-3000", "C001")
    mesa1 = Mesa(1, 4, "Ventana", True)
    mesa2 = Mesa(2, 2, "Centro", True)
    configuracion = ConfiguracionRestaurante(50, "8:00-22:00", "CFG001")
    calendario = CalendarioReservas("2023-01-01", "2023-12-31", "CAL001")
    
    # Configuración y gestión de mesas
    configuracion.agregar_mesa(mesa1)
    configuracion.agregar_mesa(mesa2)
    restaurante.configuracion = configuracion

    # Uso de métodos de Mesa
    mesa1.informar_disponibilidad()
    mesa2.informar_no_disponibilidad()
    mesa1.proveer_disposicion()
    mesa2.aplicar_nuevos_cambios(nueva_capacidad=3, nueva_ubicacion="Esquina")

    # Creación y gestión de reservas
    id_reserva = "R001"
    cliente.agregar_reserva("2023-03-15", "19:00", 4, id_reserva)
    reserva = cliente.reservas[0]
    reserva.agregar_mesa(1, 4, "Ventana", False)  # Asignar mesa a la reserva
    calendario.agregar_reserva("2023-03-15", "19:00", 4, id_reserva)  # Agregar reserva al calendario

    # Interacciones del mesero y el propietario
    mesero.hacer_reserva(calendario,"2023-03-15", "19:00", 2, "R002")
    mesero.informar_reserva_confirmada(id_reserva)
    mesero.finalizar_servicio(id_reserva)
    propietario.solicitar_confi_actual(configuracion)
    propietario.decidir_cambios(configuracion, 40)

    # Simulación de situaciones de servicio al cliente
    cliente.pedir_informacion()
    mesero.cancelar_servicio("R002")  # Asumiendo que este método cancela una reserva especificada
    reserva.cliente_no_presente()  # Marcar la reserva como no cumplida

    # Actualizaciones de configuración y notificaciones
    propietario.rectificar_cambios(nuevo_correo="nuevo@elbuensor.com", nuevo_telefono="555-1010")
    configuracion.notificar_cambios("Se ha actualizado la disposición de las mesas.")
    configuracion.actualizar_tiempo_real(60)  # Ajustar la capacidad máxima en tiempo real

if __name__ == "__main__":
    main()