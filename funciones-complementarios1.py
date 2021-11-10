"""Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo como sus parámetros y devuelva la hipotenusa del triángulo, calculada usando el teorema de Pitágoras, como resultado de la función. Incluya un programa principal que lea las longitudes de los lados más cortos de un triángulo rectángulo del usuario, use su función para calcular la longitud de la hipotenusa y muestre el resultado."""

#hipotenusa = pow(ladoa**2 + ladob**2)
ladoa = int(input("ingrese longitud del 1º lado mas corto del triángulo: "))
ladob = int(input("ingrese longitud del 2º lado mas corto del triángulo: "))

def long_hipotenusa(ladoa,ladob):
    hipotenusa = pow(ladoa**2 + ladob**2,0.5)
    return hipotenusa

longitud_hipotenusa = long_hipotenusa(ladoa,ladob)
print(f"la longitud de la hipotenusa es {longitud_hipotenusa}")
