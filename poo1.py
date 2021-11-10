"""A partir del siguiente diagrama de clases, implementá clases y métodos para mostrar atributos."""

class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"color {self.color}, ruedas {self.ruedas}"

class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f"color {self.color}, ruedas {self.ruedas}, velocidad {self.velocidad} km/h, cilindrada {self.cilindrada} cc"

vehiculo1 = Coche("azul",4,150,1200)
print(vehiculo1)
