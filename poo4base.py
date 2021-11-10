

class Agenda():
    def __init__(self):
        self.lista_contactos = []
    
    def agregarContacto(self,contacto):
        self.lista_contactos.append(contacto)
        
    def buscarContacto(self,contacto):
        return f"BUSCADOR:\n{contacto.__str__()}"

    def editarContacto(self,contacto,nuevoContacto):
        contacto = nuevoContacto
        return f"EDITOR:\n{contacto}"

    def __str__(self):
        print("AGENDA COMPLETA:\n")
        otralista = []
        for contacto in self.lista_contactos:
            otralista.append(contacto)
            return f"{otralista}"

    def salir():
        pass

class Contacto():
    def __init__(self,nombre,telefono,mail):
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail

    def __str__(self):
        return f"CONTACTO:\nNombre: {self.nombre}\nTeléfono: {self.telefono}\nMail: {self.mail}\n---"


agenda1 = Agenda()
contacto1 = Contacto("Micho",432421,"a@b.com")
contacto2 = Contacto("Tito",4324232,"b@b.com")
contacto3 = Contacto("Negro",123478,"c@b.com")
contacto4 = Contacto("Cabezón",874382,"d@b.com")
agenda1.agregarContacto(contacto1)
agenda1.agregarContacto(contacto2)
agenda1.agregarContacto(contacto3)
agenda1.agregarContacto(contacto4)

print(contacto1)
#print(agenda1)
print("-------------")
print(agenda1.buscarContacto(contacto2))
print("-------------")
print(agenda1.editarContacto(contacto3,contacto4))
print("-------------")
print(agenda1)