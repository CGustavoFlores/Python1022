print(8-6/2+1*2)
print(max("bcd","aeio","pq"))
print(list(max("bcd","aeio","pq")))
print(len(max("bcd","aeio","pq")))


def es_primo(num):
    for i in range(2 , num-1):
        if num % i == 0:
            print (i,num % i)
            return False
        else:
            print (i,num % i)
            
    return True

print(es_primo(15))


# para evitar iternaciones, solo es necesario comprobar hasta la raiz cuadrada de un numero, yq que los factores....
import time, math

def es_primo_optimizado(num):
    if num < 2:
        return False
    raiz= int(math.sqrt(num))+1
    print ( "raiz",raiz)
    for i in range (2,raiz):
        if num % i==0 :
            return False
        else:    
            print(i, raiz)
        return True
    
    
tiempo=time.time()
resultado=es_primo(1234567897)
t1=time.time()
print (resultado, tiempo, t1)
tiempo=time.time()
resultado=es_primo_optimizado(1234567897)
t1=time.time()
print (resultado, tiempo, t1)

# maximo comun divisor
def Hallar_divisores(n):
    divisores=[]
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

print ("Divisores " , Hallar_divisores(100))

def min_comun_deno(n1,n2):
    d1=Hallar_divisores(n1)
    d2=Hallar_divisores(n2)
    print(d1)
    print(d2)

    div_comunes=[]
    for i in d1:
        if i in d2:
            # el proceso los va guardando de  menor a mayor
            div_comunes.append(i)
    print(div_comunes)
    mcd=div_comunes[-1]
    return mcd

a=60
b=48
print(min_comun_deno(a,b))

        
