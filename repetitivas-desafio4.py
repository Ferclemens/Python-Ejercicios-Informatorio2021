alto = 6
ancho = 8

for i in range(alto):
    for j in range(ancho):
      if (i+j) % 2 == 0:
          print("X",end=" ")
      else:
          print("0",end=" ")
    print("")