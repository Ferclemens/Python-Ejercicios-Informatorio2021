print("----Recoleccion de colillas----")
seguir = "a"
recolectores = 0
total = 0
menosDe100 = 0
entre100y200 = 0
masDe200 = 0


while True and seguir != "x":
    recolectores += 1
    colillas = int(input("ingrese cantidad de colillas recolectadas: "))
    total += colillas
    if colillas < 100:
        menosDe100 += 1
    if colillas >= 100 and colillas <= 200:
        entre100y200 += 1
    if colillas > 200:
        masDe200 += 1
    seguir = input("para terminar de cargar presione x, sino presione cualquier tecla.")
print("total de colillas recolectadas = ",total)
print("total de recolectores : ",recolectores)
print("cantidad de personas que encontraron menos de 100 colillas ",menosDe100)
print("cantidad de personas que encontraron entre 100 y 200 colillas ",entre100y200)
print("cantidad de personas que encontraron mas de 200 colillas ",masDe200)
print("% personas que encontraron menos de 100 colillas: ",(menosDe100/recolectores)*100)
print("% personas que encontraron entre 100 y 200 colillas: ",(entre100y200/recolectores)*100)        
print("% personas que encontraron mas de 200 colillas: ",(masDe200/recolectores)*100)

