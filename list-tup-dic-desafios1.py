"""Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor."""



respuestas = []
salir = 1
while True and salir != 2:
    consulta = int(input("cuanto sabe de contaminación? del 1 al 10: "))
    respuestas.append(consulta)
    salir = int(input("seguir cargando datos? 1-Si 2-No: "))
respuestas.sort()
print(respuestas)