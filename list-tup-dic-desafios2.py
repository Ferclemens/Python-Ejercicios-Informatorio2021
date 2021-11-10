"""Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea un programa que pida números, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.

El programa termina cuando el usuario introduce un cero."""

tupla = ("residuos plástico","residuos toxicos","sobrepesca","calentamiento global","petroleo","sobrepoblación humana","cucatrap")

salir = 1
while True and salir != 0:
    resp = int(input(f"ingrese un numero entre 1 y {len(tupla)}: "))
    print(f"Uno de los factores que mas afectan a nuestros oceanos es {tupla[resp-1]}")
    salir = int(input("seguir jugando?: 1-Si 0-No: "))
print("fin del juego")