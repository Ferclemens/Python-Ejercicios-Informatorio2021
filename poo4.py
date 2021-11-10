

class Agenda():
    def __init__(self):
        self.lista_contactos = []
    
    def agregarContacto(self):
        salir = 1
        while True and salir != 0:
            print("AGREGAR CONTACTO")
            id = int(input("ingrese ID: "))
            nombre = input("ingrese nombre: ")
            telefono = int(input("ingrese telefono: "))
            mail = input("ingrese mail: ")
            contacto = Contacto(id,nombre,telefono,mail)
            self.lista_contactos.append(contacto)
            salir = int(input("continuar cargando contactos? Si - 1 / NO - 0\nSu elección: "))
        #print(self.__str__())
        
    def buscarContacto(self,id=None,nombre=None,telefono=None,mail=None):
        for a in self.lista_contactos:
            if a.id == id or a.nombre == nombre or a.telefono == telefono or a.mail == mail:
                return f"RESULTADO BUSCADOR:\n{a.__str__()}"

    def editarContacto(self,id):
        print(f"ID CONTACTO A EDITAR:\n{id}")
        #index = self.lista_contactos.id
        nuevoContacto = Agenda.agregarContacto
        contacto = nuevoContacto
        #self.lista_contactos[index] = contacto
        return f"CONTACTO EDITADO:\n{contacto}"
    
    def eliminarContacto(self, id):
        print(f"CONTACTO ELIMINADO")
        print(f"{id}")
        index = self.lista_contactos.index(id)
        self.lista_contactos.pop(index)
        return f"{self.__str__()}"

    def __str__(self):
        print("AGENDA COMPLETA:\n")
        agenda = []
        for contacto in self.lista_contactos:
            agenda.append(print(f"{contacto.__str__()}"))
        return f"{agenda}"

    def salir():
        pass

class Contacto():
    def __init__(self,id,nombre,telefono,mail):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail

    def __str__(self):
        return f"CONTACTO:\nID: {self.id}\nNombre: {self.nombre}\nTeléfono: {self.telefono}\nMail: {self.mail}\n---"

print("----------------------AGENDA PERSONAL--------------------")

agenda1 = Agenda()
agenda1.agregarContacto()
print(agenda1)

print(agenda1.buscarContacto("fer"))
print(agenda1.editarContacto(1))

"""salir = 1
while True and salir != 0:
    print("AGREGAR CONTACTO")
    nombre = input("ingrese nombre: ")
    telefono = int(input("ingrese telefono: "))
    mail = input("ingrese mail: ")
    contacto = Contacto(nombre,telefono,mail)
    agenda1.agregarContacto(contacto)
    salir = int(input("continuar cargando contactos? Si - 1 / NO - 0\nSu elección: "))"""


"""contacto1 = Contacto("Lucas",432421,"a@b.com")
contacto2 = Contacto("Maria",4324232,"b@b.com")
contacto3 = Contacto("Ramon",123478,"c@b.com")
contacto4 = Contacto("Marta",874382,"d@b.com")
contacto5 = Contacto("Julio",532453,"e@b.com")
contacto6 = Contacto("Elena",765454,"f@b.com")
contacto7 = Contacto("Marcos",896233,"g@b.com")

agenda1.agregarContacto(contacto1)
agenda1.agregarContacto(contacto2)
agenda1.agregarContacto(contacto3)
agenda1.agregarContacto(contacto4)
agenda1.agregarContacto(contacto5)
agenda1.agregarContacto(contacto6)

print(contacto1)
print(agenda1)
print("-------------")
print(agenda1.buscarContacto(contacto6))
print("-------------")
print(agenda1.editarContacto(contacto3,contacto7))
print("-------------")
print(agenda1.eliminarContacto(contacto1))
print(agenda1)"""