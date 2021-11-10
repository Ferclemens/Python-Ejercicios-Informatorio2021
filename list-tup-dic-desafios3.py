"""Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos."""

dic = {}

salir = 1

while True and salir != 0:
    nombre = input("ingrese nombre de biólogo: ")
    mail = input("ingrese mail: ")
    dic.setdefault(nombre, mail)
    salir = int(input("continuar cargando? 1-Si 0-No"))
print(dic)