class Agenda():
    def __init__(self):
        self.lista_contactos = []
    
    def menu(self):
        print("_____________AGENDA PERSONAL_____________")
        print("______________MENU AGENDA______________\n")
        print("Seleccione con 1-2-3-4-5-6 la acción requerida:\n")
        print("1 - Agregar Contacto.\n2 - Buscar Contacto.\n3 - Editar Contacto.\n4 - Eliminar Contacto.\n5 - Listar agenda completa\n6 - Cerrar Agenda.")
        eleccion = int(input("Su elección: "))
        if eleccion == 1:
            self.agregarContacto()
        elif eleccion == 2:
            id = input("seleccione ID de contacto a buscar - Enter para pasar a otro parametro.\nID:  ")
            nombre = input("seleccione NOMBRE de contacto a buscar -  Enter para pasar a otro parametro.\nNOMBRE: ")
            telefono = input("seleccione TELEFONO de contacto a buscar -  Enter para pasar a otro parametro.\nTELEFONO: ")
            mail = input("seleccione MAIL de contacto a buscar -  Enter para pasar a otro parametro.\nMAIL: ")
            print(self.buscarContacto(id,nombre,telefono,mail))
        elif eleccion == 3:
            id = int(input("seleccione ID de contacto a editar.\nID:  "))
            nvonombre = input("Nuevo NOMBRE de contacto.\nNOMBRE: ")
            nvotelefono = input("Nuevo TELEFONO de contacto.\nTELEFONO: ")
            nvomail = input("Nuevo MAIL de contacto.\nMAIL: ")
            self.editarContacto(id,nvonombre,nvotelefono,nvomail)
        elif eleccion == 4:
            id = int(input("seleccione ID de contacto a ELIMINAR.\nID:  "))
            self.eliminarContacto(id)
        elif eleccion == 5:
            self.__str__()
            self.menu()
        elif eleccion == 6:
            self.salir()

    def agregarContacto(self):
        salir = 1
        while True and salir != 0:
            print("__________AGREGAR CONTACTO__________")
            id = int(input("ingrese ID: "))
            nombre = input("ingrese nombre: ")
            telefono = input("ingrese telefono: ")
            mail = input("ingrese mail: ")
            contacto = Contacto(id,nombre,telefono,mail)
            self.lista_contactos.append(contacto)
            salir = int(input("continuar cargando contactos? 1 - SI / 0 - NO\nSu elección: "))
        self.menu()
        
    def buscarContacto(self,id=None,nombre=None,telefono=None,mail=None):
        for a in self.lista_contactos:
            if a.id == id or a.nombre == nombre or a.telefono == telefono or a.mail == mail:
                print(f"__________RESULTADO BUSCADOR__________\n{a.__str__()}")
        self.menu()
                

    def editarContacto(self,id,nvonombre,nvotelefono,nvomail):
        print(f"__________CONTACTO A EDITAR__________\n{self.lista_contactos[id-1].__str__()}")
        nuevoContacto = Contacto(id,nvonombre,nvotelefono,nvomail)
        self.lista_contactos[id-1] = nuevoContacto
        print(f"CONTACTO EDITADO:\n{nuevoContacto.__str__()}")
        self.menu()
        
    
    def eliminarContacto(self, id):
        print(f"__________CONTACTO A ELIMINAR__________")
        print(f"{self.lista_contactos[id-1].__str__()}")
        self.lista_contactos.pop(id-1)
        print(f"CONTACTO ELIMINADO CON EXITO")
        self.menu()

    def __str__(self):
        print("---------------\nAGENDA COMPLETA:\n---------------")
        for a in self.lista_contactos:
            print(a)

    def salir(self):
        print("SALIDO CON EXITO aaaaaah!")
        exit()
        
        

class Contacto():
    def __init__(self,id,nombre,telefono,mail):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail

    def __str__(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nTeléfono: {self.telefono}\nMail: {self.mail}\n--------------"


agenda1 = Agenda()
agenda1.menu()