"""Escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.

Modificá el programa anterior y dada una posición inicial p y una cantidad n, imprima el mensaje anterior para los n nombres que se encuentran a partir de la posición i."""

tupla = ("tortuga","pulpo","zardina","tiburon blanco","palometa",)
salir = 0
while True and salir != 0:
    inicio = input("ingese posición incial: ")
    fin = input("ingese posición final: ")
    for elemento in tupla[inicio:fin]:
        print(f"Hola soy {tupla[elemento]}, cuidame.")
    salir = int(input("desea salir? 1-continuar 0-Si"))


