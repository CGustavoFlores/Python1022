serie_hasta=20
fibo=[1]
for i  in range( serie_hasta):
    fibo.append(fibo[i-1]+fibo[i])
    print(fibo)
    
