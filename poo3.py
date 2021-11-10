"""Desarrollar un programa que cargue los datos de un triángulo.

Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno)."""

"""lado1 = int(input("ingrese valor de lado 1: "))
lado2 = int(input("ingrese valor de lado 2: "))
lado3 = int(input("ingrese valor de lado 3: "))"""

class Triangulo():
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    @property
    def tipoTriangulo(self):
        self.tipo = "ninguno"
        if self.lado1 == self.lado2 == self.lado3:
            self.tipo = "Equilátero"
        elif self.lado1 != self.lado2 != self.lado3:
            self.tipo = "Escaleno"
        else:
            self.tipo = "Isóseles"
        return self.tipo
    
    @property
    def ladoMasLargo(self):
        ladomaslargo = 0
        if self.lado1 > self.lado2 or self.lado1 > self.lado3:
            ladomaslargo = f"lado1 con {self.lado1} cm."
        elif self.lado2 > self.lado1 or self.lado2 > self.lado3:
            ladomaslargo = f"lado2 con {self.lado2} cm."
        elif self.lado3 > self.lado1 or self.lado3 > self.lado2:
            ladomaslargo = f"lado3 con {self.lado3} cm."
        else:
            ladomaslargo = "ninguno, son iguales los lados."
        return ladomaslargo

    def __str__(self):
       return f"el triángulo es del tipo {self.tipoTriangulo} y el lado mas largo es {self.ladoMasLargo}"

triangulo1 = Triangulo(10,9,10)
print(triangulo1)