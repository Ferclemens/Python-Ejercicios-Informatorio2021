# Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
# Además deberá mostrar un menú con las siguientes opciones.

    # Añadir contacto

    # Lista de contactos

    # Buscar contacto

    # Editar contacto

    # Cerrar agenda



class Agenda:
    def __init__(self):
        self.contacto = Contacto()
    
    def menu(self):
        print()
        menu = [
            ['                ------ Agenda de Contactos------'],
            ['                |      1- Añadir Contacto      |'],
            ['                |      2- Lista Contacto       |'],
            ['                |      3- Buscar Contacto      |'],
            ['                |      4- Editar Contacto      |'],
            ['                |      5- Cerrar Agenda        |'],
            ['                --------------------------------']
        ]
        for i in range(7):
            print(menu[i][0])
        opcion = int(input("Ingrese la opcion que desea ejecutar. "))
        if opcion == 1:
            self.contacto.datos()
        elif opcion == 2:
            self.contacto.mostrar()
        elif opcion == 3:
            self.contacto.buscar()
        elif opcion == 4:
            self.contacto.editar()
        elif opcion == 5:
            print("Cerrando agenda...")
            exit()
        self.menu()
        

class Contacto:
    def __init__(self):
        self.contactos = []

    def datos(self):
        nombre = (input("Ingrese el nombre de contacto: "))
        telefono = int(input("Ingrese el telefono: "))
        email = (input("Ingrese el email: "))
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email })
        
    
    def mostrar (self):
        if len(self.contactos) == 0:
            print("No hay contactos guardados.")
        else:
            for i in range(len(self.contactos)):
                print(self.contactos[i]["nombre"])

    
    def buscar(self):
        nombreContacto = input("Ingrese el nombre del contacto buscado")
        for i in range(len(self.contactos)):
            if nombreContacto == self.contactos[i]["nombre"]:
                print("Nombre:",self.contactos[i]["nombre"])
                print("Telefono:",self.contactos[i]["telefono"])
                print("Email:",self.contactos[i]["email"])
                return i
                

    def editar(self):
        data= self.buscar()
        condition = True
        while condition == True:
            print("EDITAR")
            print("1-Editar nombre:")
            print("2-Editar telefono:")
            print("3-Editar email:")
            print("4-Cerrar")
            opcion = int(input("Seleccionar la opcion"))
            if opcion == 1:
                nombreEditar = input("Ingrese nombre a editar ")
                self.contactos[data]["nombre"] = nombreEditar
            elif opcion == 2:
                telefonoEditar = input("Ingrese nuevo numero ")
                self.contactos[data]["telefono"] = telefonoEditar
            elif opcion == 3:
                emailEditar = input("Ingrese mail a editar ")
                self.contactos[data]["email"] = emailEditar
            elif opcion == 4:
                break

agenda = Agenda()
agenda.menu()


