"""Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.

    Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra mostrando el nombre de su clase y sus atributos.

    Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor"""

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
        return Vehiculo.__str__(self) + f", velocidad {self.velocidad} km/h, cilindrada {self.cilindrada} cc"

class Camioneta(Coche):
    def __init__(self, color, ruedas,velocidad,cilindrada,carga):
        Coche.__init__(self,color,ruedas,velocidad,cilindrada)
        self.carga = carga
    
    def __str__(self):
        return Coche.__str__(self) + f", carga máxima {self.carga} kg."

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self,color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return Vehiculo.__str__(self) + f", tipo {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        Bicicleta.__init__(self,color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Bicicleta.__str__(self) + f", velocidad {self.velocidad} km/h, cilindrada {self.cilindrada} cc"

coche1 = Coche("rojo",4,120,1600)
camioneta1 = Camioneta("blanca",4,90,1800,600)
bici1 = Bicicleta("verde",2,"deportiva")
moto1 = Motocicleta("azul",2,"urbana",100,125)
coche2 = Coche("Amarillo",4,180,2200)

lista = [coche1,camioneta1,bici1,moto1,coche2]

def catalogar(lista,ruedas=None):
        count = 0
        for elemento in lista:
            if ruedas != None and elemento.ruedas == ruedas:
                count += 1
                print(type(elemento).__name__,f"=> {elemento}")
            elif ruedas == None:
                print(type(elemento).__name__,f"=> {elemento}")
        print(f"Se han encontrado {count} vehículos con {ruedas} ruedas.")

resutado = catalogar(lista,4)
print(resutado)

#print(coche2.ruedas)

