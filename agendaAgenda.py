from agendaContacto import Contacto
from agendaMenu import Menu

class Agenda():
    def __init__(self):
        self.lista_contactos = []
    
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
        Menu.menu(self)
        
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

agenda1 = Agenda()
