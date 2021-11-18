class Contacto():
    def __init__(self,id,nombre,telefono,mail):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail

    def __str__(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nTeléfono: {self.telefono}\nMail: {self.mail}\n--------------"
