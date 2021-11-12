

class Agenda():
    def __init__(self):
        self.lista_contactos = []
    
    def menu(self):
        print("------------MENU AGENDA------------")
        print("Seleccione con 1-2-3-4-5 la acción requerida:\n")
        print("1 - Agregar Contacto.\n2 - Buscar Contacto.\n3 - Editar Contacto.\n4 - Eliminar Contacto.\n5 - Cerrar Agenda.")
        eleccion = int(input("Su elección: "))
        if eleccion == 1:
            self.agregarContacto()
        elif eleccion == 2:
            id = int(input("seleccione ID de contacto a editar - Enter para buscar por otro parametro."))
            nombre = input("seleccione NOMBRE de contacto a editar - Enter para buscar por otro parametro.")
            telefono = int(input("seleccione TELEFONO de contacto a editar - Enter para buscar por otro parametro."))
            mail = input("seleccione MAIL de contacto a editar - Enter para buscar por otro parametro.")
            self.buscarContacto(self,id,nombre,telefono,mail)
        elif eleccion == 3:
            self.editarContacto()
        elif eleccion == 4:
            self.eliminarContacto()
        else:
            pass

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
            salir = int(input("continuar cargando contactos? 1 - SI / 0 - NO\nSu elección: "))
        self.menu()
        
    def buscarContacto(self,id=None,nombre=None,telefono=None,mail=None):
        for a in self.lista_contactos:
            if a.id == id or a.nombre == nombre or a.telefono == telefono or a.mail == mail:
                return f"RESULTADO BUSCADOR:\n{a.__str__()}"

    def editarContacto(self,id,nvonombre,nvotelefono,nvomail):
        print(f"CONTACTO A EDITAR:\n{self.lista_contactos[id-1].__str__()}")
        nuevoContacto = Contacto(id,nvonombre,nvotelefono,nvomail)
        self.lista_contactos[id-1] = nuevoContacto
        return f"CONTACTO EDITADO:\n{nuevoContacto.__str__()}"
    
    def eliminarContacto(self, id):
        print(f"CONTACTO A ELIMINAR")
        print(f"{self.lista_contactos[id].__str__()}")
        self.lista_contactos.pop(id)
        print(f"CONTACTO ELIMINADO CON EXITO")
        return f"{self.lista_contactos.__str__()}"

    def __str__(self):
        print("AGENDA COMPLETA:")
        for a in self.lista_contactos:
            print(a)

    def salir():
        pass
        

class Contacto():
    def __init__(self,id,nombre,telefono,mail):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail

    def __str__(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nTeléfono: {self.telefono}\nMail: {self.mail}\n----------"

print("------------AGENDA PERSONAL------------")

agenda1 = Agenda()
agenda1.menu()
"""agenda1.agregarContacto()
agenda1.__str__()
agenda1.buscarContacto(telefono=654)
agenda1.editarContacto(1,nvonombre="Roman",nvotelefono=543,nvomail="fdasfds")
agenda1.eliminarContacto(2)
agenda1.__str__()"""

#print(agenda1.buscarContacto(nombre="fer"))
#print(agenda1.editarContacto(1,nvonombre="ramon",nvotelefono=555,nvomail="ytr"))
#print(agenda1)

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