"""Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en diferentes ciudades de Argentina durante la cuarentena. Luego la función debe devolver dos listas ordenadas. La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena."""

dic_lista = []
continuar = 1
while True and continuar != "2":
    datos = []
    ciudades = str(input("Ingrese nombre de ciudad: "))
    arboles = int(input("Ingrese cantidad de arboles plantados: "))
    datos += [ciudades,arboles]
    dic_lista.append(datos)
    continuar = input("Seguir cargando? 1-Si / 2-No.")
 
def separar(lista):
    mas_de_100 = []
    igual_o_menos_de_100 = []
    for i in lista:
        if i[1] > 100:
            mas_de_100.append(i[0])
        elif i[1] <= 100:
            igual_o_menos_de_100.append(i[0])
    return f"Las ciudades que plantaron mas de 100 arboles son {mas_de_100}\nLas ciudades que plantaron menos de 100 arboles son {igual_o_menos_de_100}\nHan plantado mas de 100 arboles {len(mas_de_100)} ciudades."

print(dic_lista)
resultado = separar(dic_lista)
print(resultado)