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

        # Inicializa las entidades principales de la aplicación.
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

    # Configura la interfaz de usuario, creando las pestañas y sus contenidos.
    def initUI(self):

        # Configura el encabezado y los estilos de la aplicación.
        self.headerLabel = QLabel(f"Bienvenido al Restaurante 'El Buen Sabor' - Calle Principal #123")
        self.headerLabel.setStyleSheet("""
                                            QLabel {
                                                color: black;
                                                background-color: gray;
                                                font-size: 26px; 
                                                font-weight: bold;
                                                padding: 30px 0px;
                                            }
                                        """)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.headerLabel)
        self.layout.addWidget(self.tabWidget)
        centralWidget = QWidget()
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)

        # Configura la pestaña "Hacer Reserva" con los campos necesarios para realizar una reserva.
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
        
        # Configura la pestaña "Ver Reserva" para mostrar las reservas existentes.
        layoutReservas = QVBoxLayout()
        self.verReservasBtn = QPushButton("Ver Reservas")
        self.layoutVerReserva = QTextEdit(self)
        self.layoutVerReserva.setReadOnly(True)  # Hacerlo solo lectura
        layoutReservas.addWidget(self.verReservasBtn)
        layoutReservas.addWidget(self.layoutVerReserva)
        self.tabVerReserva.setLayout(layoutReservas)
        
        # Configura la pestaña "Gestionar Capacidad" para ver y ajustar la capacidad del restaurante.
        layoutGestionarCapacidad = QVBoxLayout()
        self.layoutVerCapacidad = QTextEdit(self)
        self.layoutVerCapacidad.setReadOnly(True)  # Hacerlo solo lectura
        self.verCapacidadBtn = QPushButton("Ver configuración actual")
        layoutGestionarCapacidad.addWidget(self.verCapacidadBtn)
        layoutGestionarCapacidad.addWidget(self.layoutVerCapacidad)

        layoutGestionarCapacidad.addWidget(QLabel("Nueva Capacidad:"))
        self.capacidadInput = QLineEdit()
        layoutGestionarCapacidad.addWidget(self.capacidadInput)
        layoutGestionarCapacidad.addWidget(QLabel("Nueva Fecha de operación:"))
        self.horarioInput = QLineEdit()
        layoutGestionarCapacidad.addWidget(self.horarioInput)
        self.actualizarCapacidadBtn = QPushButton("Actualizar capacidad")
        layoutGestionarCapacidad.addWidget(self.actualizarCapacidadBtn)

        self.disposicionBtn = QPushButton("Consultar dispocisión")
        layoutGestionarCapacidad.addWidget(self.disposicionBtn)

        self.tabGestionarCapacidad.setLayout(layoutGestionarCapacidad)
        
        # Conecta los botones a sus respectivos métodos.
        self.reservarBtn.clicked.connect(self.hacerReserva)
        self.verReservasBtn.clicked.connect(self.mostrarReserva)
        self.verCapacidadBtn.clicked.connect(self.gestionarCapacidad)
        self.actualizarCapacidadBtn.clicked.connect(self.actualizarCambios)
        self.disposicionBtn.clicked.connect(self.disposicion)

    # Crea una reserva basada en la información proporcionada por el usuario.
    def hacerReserva(self):
        nombreCliente = self.nombreCliente.text()
        correoCliente = self.correoCliente.text()
        telefonoCliente = self.telefonoCliente.text()
        self.idCliente += 1
        fecha = self.fechaInput.text()
        hora = self.horaInput.text()
        numero_personas = int(self.personasInput.text())
        self.idReserva += 1
        
        # Lógica para crear una reserva y actualizar la información mostrada al usuario.
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
            
        self.nombreCliente.clear()
        self.correoCliente.clear()
        self.telefonoCliente.clear()
        self.fechaInput.clear()
        self.horaInput.clear()
        self.personasInput.clear()

    # Prepara y guarda la información de las reservas existentes.
    def verReserva(self, mesajeReservaSolicitada, informacion):
        self.infoVerReservas += informacion + "\n" + mesajeReservaSolicitada + "\n\n"

    # Muestra la información acumulada de las reservas en la interfaz de usuario.
    def mostrarReserva(self):
        if(self.infoVerReservas == ""):
            self.layoutVerReserva.setText("No hay reservas registradas")
        else:
            self.layoutVerReserva.setText(self.infoVerReservas)

    # Solicita y muestra la configuración actual del restaurante.  
    def gestionarCapacidad(self):
        confActual = self.propietario.solicitar_confi_actual(self.configuracion)
        self.layoutVerCapacidad.setText(confActual)

    # Aplica y refleja los cambios realizados a la capacidad y horarios del restaurante.
    def actualizarCambios(self):
        cambios = self.propietario.decidir_cambios(self.restaurante, self.capacidadInput, self.horarioInput)
        self.configuracion.capacidad_maxima = self.capacidadInput.text()
        self.configuracion.horarios_operacion = self.horarioInput.text()
        self.layoutVerCapacidad.setText("")
        self.capacidadInput.clear()
        self.horarioInput.clear()
        self.mesajeActualizacion = QMessageBox()
        self.mesajeActualizacion.about(self, "Cambios", cambios)

    # Consulta y muestra la disposición actual de las mesas en el restaurante.
    def disposicion(self):
        capacidad = self.configuracion.consultar_disposicion()
        self.mesajeDisposicion = QMessageBox()
        self.mesajeDisposicion.about(self, "Disposición", capacidad)

def main():
    app = QApplication(sys.argv)
    mainWindow = RestauranteApp()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
