import random
censo=[]
alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZAEIOU"
numero=0
print("creando cencos....")
for i in range(50):
    aumento=random.randint(1,2)
    numero += aumento  
    letras= random.sample(alfabeto,5)
    nombre="".join(letras)
    edad=random.randint(18,99)
    impuestos= random.choice((True,True,True, False))
    censo.append([numero, nombre,edad, impuestos])
    print(censo)
    
    





def busqueda_numero(lista, elemento):
    inicio=0
    final=len(lista)-1
    while inicio <= final:
        medio=(inicio+final)//2
        if lista[medio]== elemento:
            return lista[medio]
        elif lista[medio] > elemento:
            inicio=medio+1
        elif lista[medio] < elemento:
            final=medio-1
    return None

def busqueda_nombre(lista,elemento):
    # busqueda lineal
    encontrados=[]
    for registro in lista:
        if registro[1] in elemento:
            encontrados.append((registro))
    if len(encontrados) == 0:
        return None
    else:
        return encontrados
    
def muestra_registro(registro):
    if registro == None:
        print("No existe registro con ese dato")
    else:
        print("--------------------------")
        print("Numero", registro[0])
        print("Nombre", registro[1])
        print("Edad", registro[2])
        print("Impuestos", registro[3])        

def menu():
        print("--------------------------")
        print("---CENSO DE POBLACION-----")
        print("--------------------------")
        print("1. Buscar por Numero")
        print("2- Buscar por Nombre")
        print("3- Salir")
        opcion=""
        while opcion not in ("1","2","3"):
            opcion= input("--> ")
            return opcion
        
        

while True:
    op = menu()
    if op == "1":
        try:
            numero= int(input("introduce numero: "))
        except ValueError:
            print("Introduzca un nro. entero")
        else:
            registro=busqueda_numero(censo, numero)
            muestra_registro(registro)
    elif op == "2":
        nombre= input("Introduce nombre: ").upper()
        registros =  busqueda_nombre(censo, nombre)
        if registros == None:
            print("No existe registro con ese dato")
        else:
            for registro in registros:
                muestra_registro(registro)  
    elif op == "3":
        break
        
            
    
    