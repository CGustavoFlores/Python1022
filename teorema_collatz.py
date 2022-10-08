def collatz(num):
    secuencia=[]
    while num > 1:
        if num % 2 == 0:
            # si es par, se divide entre 2
            num=num/2
        else:
            num=(num*3)+1
        secuencia.append(num)
    return(secuencia)
print (collatz(50))
