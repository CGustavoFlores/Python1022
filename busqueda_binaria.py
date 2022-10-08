# se aplica si los datos estan ordenados

def busqueda_binaria(lista, elemento):
    inicio=0
    fin= len(lista)-1
    
    while inicio <= fin:
        medio= (inicio+fin)//2
        if lista[medio] == elemento:
            return True
        elif lista[medio] < elemento:
            inicio=medio +1
        elif lista[medio]  > elemento:
            fin=medio-1
    return False

lista=[]
for i in range(100000000):
    lista.append(i)
elemento=65
#print (lista)

print(busqueda_binaria(lista, elemento))