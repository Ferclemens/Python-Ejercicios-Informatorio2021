import agendaAgenda


class Menu():
    def __init__(self):
        pass

    def menu(self):
        print("_____________AGENDA PERSONAL_____________")
        print("______________MENU AGENDA______________\n")
        print("Seleccione con 1-2-3-4-5-6 la acción requerida:\n")
        print("1 - Agregar Contacto.\n2 - Buscar Contacto.\n3 - Editar Contacto.\n4 - Eliminar Contacto.\n5 - Listar agenda completa\n6 - Cerrar Agenda.")
        eleccion = int(input("Su elección: "))
        if eleccion == 1:
            agendaAgenda.Agenda.agregarContacto(self)
            Menu.menu(self)
        elif eleccion == 2:
            id = input("seleccione ID de contacto a buscar - Enter para pasar a otro parametro.\nID:  ")
            nombre = input("seleccione NOMBRE de contacto a buscar -  Enter para pasar a otro parametro.\nNOMBRE: ")
            telefono = input("seleccione TELEFONO de contacto a buscar -  Enter para pasar a otro parametro.\nTELEFONO: ")
            mail = input("seleccione MAIL de contacto a buscar -  Enter para pasar a otro parametro.\nMAIL: ")
            resultado = agendaAgenda.Agenda.buscarContacto(self,id,nombre,telefono,mail)
            print(resultado)
            Menu.menu(self)
        elif eleccion == 3:
            id = int(input("seleccione ID de contacto a editar.\nID:  "))
            nvonombre = input("Nuevo NOMBRE de contacto.\nNOMBRE: ")
            nvotelefono = input("Nuevo TELEFONO de contacto.\nTELEFONO: ")
            nvomail = input("Nuevo MAIL de contacto.\nMAIL: ")
            agendaAgenda.Agenda.editarContacto(self,id,nvonombre,nvotelefono,nvomail)
            Menu.menu(self)
        elif eleccion == 4:
            id = int(input("seleccione ID de contacto a ELIMINAR.\nID:  "))
            agendaAgenda.Agenda.eliminarContacto(self,id)
            Menu.menu(self)
        elif eleccion == 5:
            agendaAgenda.Agenda.__str__(self)
            Menu.menu(self)
        elif eleccion == 6:
            agendaAgenda.Agenda.salir(self)
