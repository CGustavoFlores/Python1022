palabras=["banco", "escritorio", "hombre"]
capitalize= [ palabra.title() for palabra in palabras if "r" in palabra]
print (capitalize)
# generar nros pares sin list-compreshion

matriz=[]
while len(matriz) < 100:
    matriz=[ i*2 for i in range(100) ]
print ("con while " ,matriz)


pares=[]
for i in range(100):
    if i % 2  == 0:
        pares.append(i)
print ("con for " , pares)

# con list comprehsion

pares=[pares for pares in range(100) if pares % 2 == 0  ]
print ("pares compresion", pares)