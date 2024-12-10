def suma(a,b):
    return a+b 
try:
    a = int(input("ingrese un número : "))
    b = int(input("ingrese un número : "))
    
    respuesta = suma(a,b)
    print(respuesta)
except ValueError:
    print("error numero no valido")
