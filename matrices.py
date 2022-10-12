from wsgiref.validate import validator


filas= int(input("Ingrese filas: "))
columnas= int(input("Ingrese columnas: "))
matriz=[]
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor= float(input("Fila {} , Colunna {} : ".format(i+1, j+1)))
        matriz[i].append(valor)
         
        
print ()
for fila in matriz:
    print("[", end=" ")
    for elemento in fila:
        print("{}".format(elemento), end=" ")
    print("]")
print()

