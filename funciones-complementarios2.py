"""En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base de $40.00, más $15.00 por cada 140 metros recorridos. Escriba una función que tome la distancia recorrida (en kilómetros) como su único parámetro y devuelva la tarifa total como su único resultado. Escriba un programa principal que use la función.


Sugerencia: Utilice constantes para presentar la base y la porción variable de las tarifas así el programa podrá actualizar fácilmente cuando las tasas aumentan."""

tarifa_base = 40
plus = 15
dist_plus = 140

distancia = int(input("ingrese distancia a recorrer en km: "))
def calcularTarifa():
    tarifa_total = tarifa_base + (plus*(distancia*1000)/dist_plus)
    return tarifa_total

tarifa_viaje = calcularTarifa()
print(f"La tarifa del viaje es ${round(tarifa_viaje,2)}")
