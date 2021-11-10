"""Escriba una función que tome tres números como parámetros y devuelva el valor medio de esos parámetros como resultado. Incluya un programa principal que lea tres valores del usuario y muestre su mediana.


Sugerencia: El valor medio es el medio de los tres valores cuando se ordenan en orden ascendente. Se puede encontrar usando declaraciones if, o con un poco de creatividad matemática."""

x = int(input("ingrese un valor: "))
y = int(input("ingrese otro valor: "))
z = int(input("ingrese ultimo valor: "))

valores = []
def media(x,y,z):
    valores.append(x)
    valores.append(y)
    valores.append(z)
    valores.sort()
    print(f"El valor medio es {valores[1]}")

def mediana(x,y,z):
    print(f"La media de los valores ingresados es {(x+y+z)/3}") 


media(x,y,z)
mediana(x,y,z)