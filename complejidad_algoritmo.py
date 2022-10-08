# sumar n numeros. una forma rapida es :
# suma de n numeros= (n/2)*(n+1)
import time, os
def suma_lineal(numero):
    for i in  range(1,numero):
        suma=+i
    return suma

def suma_constante(numero):
    suma=(numero/2) * (numero+1)
    return suma 

cantidad=1000000
for i in range(4):
    t0=time.time()
    suma1=suma_lineal(cantidad)
    t1= time.time()
    suma2=suma_constante(cantidad)
    t2=time.time()
    
    print("lineal " + "{}  -  {}".format(suma1,t1-t0))
    print("constante " + "{}  -  {}".format(suma2,t2-t1))
    
    cantidad*=10
    
