# contar vehiculos que pasan por autopista, y determinar cuantos son autos , y cuantos son motos
# contar vehciulco, por cada vehiculo contar ruedas, si tiene 4, sumar auto, si tiene 2 sumar motod
# se recibe como parametro la cantidad de coches  y la cantidad de ruedas, entonces hay que determinar
# cuantos son autos y cuantos son motos

# 1. algoritmocuadratico, menos eficiente (usa 2 for)
from this import d


def algo1( vehiculos, ruedas):
# complejidad cuadrativa
    for coches in range(vehiculos+1):
        for motos in range(vehiculos+1):
            print (coches, motos)
            if ((coches + motos) == vehiculos and ((coches*4)+ (motos *2))==ruedas):
                return coches, motos
    return None             


def algo2(vehiculos, ruedas):
    for coches in range(vehiculos+1):
        motos=vehiculos - coches
        if coches * 4 + motos *2 == ruedas:
            return coches, motos
    return None

algo2(1000,15000)
algo1(1000,15000)