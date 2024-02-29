from Restaurante import Restaurante
from Empleado import Empleado
from Mesero import Mesero
from Propietario import Propietario
from Cliente import Cliente
from Reserva import Reserva
from Mesa import Mesa
from CalendarioReservas import CalendarioReservas
from ConfiguracionRestaurante import ConfiguracionRestaurante
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout, QTextEdit, QMessageBox

class RestauranteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sistema de reservas de un restaurante')
        self.setGeometry(1000, 400, 1000, 500)
        
        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)
        
        self.tabHacerReserva = QWidget()
        self.tabVerReserva = QWidget()
        self.tabGestionarCapacidad = QWidget()
        
        self.tabWidget.addTab(self.tabHacerReserva, "Hacer Reserva")
        self.tabWidget.addTab(self.tabVerReserva, "Ver Reservas")
        self.tabWidget.addTab(self.tabGestionarCapacidad, "Gestionar Capacidad")

        # Inicialización de entidades
        self.restaurante = Restaurante("El Buen Sabor", "Calle Principal #123")
        self.propietario = Propietario("Juan Pérez", "ID001", "juan@elbuensor.com", "555-1000", True, True)
        self.mesero = Mesero("Ana Gómez", "ID002", "ana@elbuensor.com", "555-2000", ["Mañana"], "Sección A")
        self.configuracion = ConfiguracionRestaurante(50, "8:00-22:00", "CFG001")
        self.calendario = CalendarioReservas("2023-01-01", "2023-12-31", "CAL001")

        self.idCliente = 0
        self.idReserva = 0
        self.numMesa = 0

        self.infoVerReservas = ""

        self.initUI()

    def initUI(self):

        # Agregar encabezado con información del restaurante
        self.headerLabel = QLabel(f"Bienvenido al Restaurante 'El Buen Sabor' - Calle Principal #123")
        self.headerLabel.setStyleSheet("font-size: 26px; font-weight: bold;")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.headerLabel)
        
        # Asegúrate de añadir las pestañas al layout principal
        self.layout.addWidget(self.tabWidget)
        # Establece el layout principal en el widget central
        centralWidget = QWidget()
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)

        # Tab Hacer Reserva
        layoutHacerReserva = QFormLayout()
        self.labelCliente = QLabel()
        self.labelInfoReserva = QLabel()
        self.nombreCliente = QLineEdit()
        self.correoCliente = QLineEdit()
        self.telefonoCliente = QLineEdit()
        self.fechaInput = QLineEdit()
        self.horaInput = QLineEdit()
        self.personasInput = QLineEdit()
        self.reservarBtn = QPushButton("Reservar")

        layoutHacerReserva.addRow("Información del cliente", self.labelCliente)

        layoutHacerReserva.addRow("Nombre:", self.nombreCliente)
        layoutHacerReserva.addRow("Correo:", self.correoCliente)
        layoutHacerReserva.addRow("Telefono:", self.telefonoCliente)

        layoutHacerReserva.addRow("Información de la reserva", self.labelInfoReserva)

        layoutHacerReserva.addRow("Fecha:", self.fechaInput)
        layoutHacerReserva.addRow("Hora:", self.horaInput)
        layoutHacerReserva.addRow("Número de Personas:", self.personasInput)
        layoutHacerReserva.addRow(self.reservarBtn)
        self.tabHacerReserva.setLayout(layoutHacerReserva)
        
        # Tab Ver Reserva
        layoutReservas = QVBoxLayout()
        self.verReservasBtn = QPushButton("Ver Reservas")
        self.layoutVerReserva = QTextEdit(self)
        self.layoutVerReserva.setReadOnly(True)  # Hacerlo solo lectura
        layoutReservas.addWidget(self.verReservasBtn)
        layoutReservas.addWidget(self.layoutVerReserva)
        self.tabVerReserva.setLayout(layoutReservas)
        
        # Tab Gestionar Capacidad
        layoutGestionarCapacidad = QVBoxLayout()
        self.capacidadInput = QLineEdit()
        self.actualizarCapacidadBtn = QPushButton("Actualizar Capacidad")
        layoutGestionarCapacidad.addWidget(QLabel("Nueva Capacidad:"))
        layoutGestionarCapacidad.addWidget(self.capacidadInput)
        layoutGestionarCapacidad.addWidget(self.actualizarCapacidadBtn)
        self.tabGestionarCapacidad.setLayout(layoutGestionarCapacidad)
        
        # Conectar botones a acciones
        
        self.reservarBtn.clicked.connect(self.hacerReserva)
        self.actualizarCapacidadBtn.clicked.connect(self.gestionarCapacidad)
        self.verReservasBtn.clicked.connect(self.mostrarReserva)

    def hacerReserva(self):
        nombreCliente = self.nombreCliente.text()
        correoCliente = self.correoCliente.text()
        telefonoCliente = self.telefonoCliente.text()
        self.idCliente += 1
        fecha = self.fechaInput.text()
        hora = self.horaInput.text()
        numero_personas = int(self.personasInput.text())
        # Aquí podrías generar un ID de reserva único, por ejemplo:
        self.idReserva += 1
        
        # Crear la nueva reserva y agregarla a las entidades relevantes
        cliente = Cliente(nombreCliente, correoCliente, telefonoCliente, self.idCliente)
        
        mesajeReservaSolicitada = cliente.solicitar_reserva(fecha, hora, numero_personas)

        self.verReserva(mesajeReservaSolicitada, cliente.pedir_informacion())

        self.mesajeReservaSolicitada = QMessageBox()
        self.mesajeReservaSolicitada.about(self, "", mesajeReservaSolicitada)

        mesajeReservaHecha = self.mesero.hacer_reserva(self.calendario, fecha, hora, numero_personas, self.idReserva)

        self.mesajeConfirmacion = QMessageBox()

        self.numMesa += 1
        mesa = Mesa(self.numMesa, numero_personas, "", True)
        self.configuracion.agregar_mesa(mesa)
        disponibilidad = self.configuracion.verificar_disponibilidad()
        if(len(self.calendario.reservas) > 1):
            print(self.calendario.reservas[self.numMesa -2].fecha)
            print(self.calendario.reservas[self.numMesa -2].hora)
            if((self.calendario.reservas[self.numMesa -2].fecha == fecha) and (self.calendario.reservas[self.numMesa -2].hora == hora)):
                disponibilidad = False
            else:
                disponibilidad = True

        if(disponibilidad == True):
            mesa.informar_disponibilidad()
            self.configuracion.reserva_confirmada(self.numMesa)
            mensajeConfirmacion = self.mesero.informar_reserva_confirmada(self.idReserva)
        else:
            mesa.informar_no_disponibilidad()
            self.configuracion.reserva_no_disponible(self.numMesa)
            mensajeConfirmacion = self.mesero.informar_reserva_no_disponible(fecha, hora)
        
        self.mesajeConfirmacion.about(self, cliente.nombre, mensajeConfirmacion)
            
        # Actualizar la interfaz de usuario según sea necesario, por ejemplo, limpiar campos de entrada
        self.nombreCliente.clear()
        self.correoCliente.clear()
        self.telefonoCliente.clear()
        self.fechaInput.clear()
        self.horaInput.clear()
        self.personasInput.clear()

    def verReserva(self, mesajeReservaSolicitada, informacion):
        self.infoVerReservas += informacion + "\n" + mesajeReservaSolicitada + "\n\n"

    def mostrarReserva(self):
        if(self.infoVerReservas == ""):
            self.layoutVerReserva.setText("No hay reservas registradas")
        else:
            self.layoutVerReserva.setText(self.infoVerReservas)
        
    def gestionarCapacidad(self):
        confActual = self.propietario.solicitar_confi_actual(self.configuracion)
        print(confActual)

        disposicion = self.configuracion.consultar_disposicion()
        print(disposicion)

        cambios = self.propietario.decidir_cambios(self.restaurante, 30, "9:00-20:00")
        print(cambios)

def main():
    app = QApplication(sys.argv)
    mainWindow = RestauranteApp()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
