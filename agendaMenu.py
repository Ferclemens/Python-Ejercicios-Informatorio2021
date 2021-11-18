from agendaAgenda import agenda1
from agendaContacto import Contacto


class Menu():
    def __init__(self):
        self.menu = menu()

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

menu1 = Menu()