import csv, operator

with open("C:\SISTEMAS\PYTHON\PRACTICAS\LISTA_ARTICULOS.CSV") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        print(reg)  