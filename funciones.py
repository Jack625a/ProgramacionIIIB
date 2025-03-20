#def nombreFuncion(parametros)

def sumar(a,b):
    return a+b

#Llamar una funcion
resultado=sumar(8,5)
print(resultado)
print(sumar(1,5))

#Funciones sin parametros
def bienvenida():
    print("Bienvenido")

bienvenida()
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese un numero: "))
#print(sumar(num1,num2))

#Funcion para crear una calculadora simples(+-*/)
def calculadora(a,b,operacion):
    if operacion=='suma':
        return a+b
    elif operacion=='resta':
        return a-b
    elif operacion=='multiplicar':
        return a*b
    elif operacion=='dividir':
        return a/b
    else:
        print("error")


#Bucle para la calculadora
while True:
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion=input("Elija la operacion que desea realizar")
    numero=float(input("Ingrese un numero: "))
    numero2=float(input("Ingrese un numero: "))
    if opcion=="1":
        print(calculadora(numero,numero2,"sumar"))
    elif opcion=="2":
        print(calculadora(numero,numero2,"restar"))
    elif opcion=="3":
        print(calculadora(numero,numero2,"multiplicar"))
    elif opcion=="4":
        print(calculadora(numero,numero2,"dividir"))
    elif opcion=="5":
        print("GRACIAS POR UTILIZAR LA CALCULADORA")
        break