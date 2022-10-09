palabras=["banco", "escritorio", "hombre"]
capitalize= [ palabra.title() for palabra in palabras if "r" in palabra]
print (capitalize)

matriz=[]
while len(matriz) < 100:
    matriz=[ i*2 for i in range(100) ]
print (matriz)