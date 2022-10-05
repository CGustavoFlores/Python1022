serie_hasta=25
fibo=[1]
for i  in range( serie_hasta):
    fibo.append(fibo[i-1]+fibo[i])
    print(fibo)
    
adicionar= lambda a,b:a+b

print(adicionar(5,8))


# packing/unpacking
def sumar(a,b,c,d):
    print(a+b+c+d)
    
n=[1,2,3,4]
# como pasar numeros a sumar
# 1. no hacer, es muy malo
print(sumar(n[1],n[2],n[3],n[4]))
# 2- la mejor forma es desempacando
a,b,c,d=n  # hacemos unpacking
# lo anterior se pude hacer:
a,b,c,d = n
print(sumar(a,b,c,d))
# agrupamiento
n=[1,2,3,4]
print(sumar(*n))