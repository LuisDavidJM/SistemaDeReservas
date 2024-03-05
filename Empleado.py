class Empleado:
    def __init__(self, nombre, identificacion, correoElectronico, telefono):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correoElectronico = correoElectronico
        self.telefono = telefono

    # Permite actualizar el correo electrónico y/o el número de teléfono del empleado.
    # Devuelve un mensaje indicando qué información se actualizó.
    def rectificarCambios(self, nuevo_correo=None, nuevo_telefono=None):
        if nuevo_correo:
            self.correoElectronico = nuevo_correo
            return f"Correo electrónico actualizado a {self.correoElectronico} para el empleado {self.nombre}."
        
        if nuevo_telefono:
            self.telefono = nuevo_telefono
            return f"Teléfono actualizado a {self.telefono} para el empleado {self.nombre}."
        
        if not nuevo_correo and not nuevo_telefono:
            return "No se proporcionaron nuevos datos para actualizar."
