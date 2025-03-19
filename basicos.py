#Comentario en Python
#Basico de Python
#Tipos de Datos
#Datos Simples
nombre="Kevin Arroyo" #variable con tipo de dato String
numero=12
encender=True #False
#Datos Compuestos
#Listas [] , Tuplas (), Diccionarios {}
colores=["Rojo","Verde","Azul"]
colores2=("Rojo","Amarillo","Rosado")
estudiantes={
    nombre:"Kevin"
    }
#Operadores
#Operadores Aritmeticos
#suma, resta, multiplicacion, division, modulo

#Operadores Logicos(1,0)
#mayor, menor, igual, diferente
#Condicionales
#if,else,elif
n=15
m=18
if n>m:         
    print("Verdadero")
else:
    print("Falso")

#Bucles
#for, while
#Ej1. Crear la tabla de multiplicar del 7
#for iterar in range(11):
 #   print(f"{iterar}x7= {iterar*7}")

#Ej1. Crear la tabla de multiplicar de cualquier digito ingresado por teclado

#b=input("Ingrese un numero: ")

#While
#while condicion
# bloque 
a=1
while a<=10:
    print(a)
    a+=1
opcion=int(input("Seleccione una opcion: "))
print(opcion)
control=True
while control:
    print("Menu de ocpiones")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Opcion 3")
    print("4. Salir")
    opcion=int(input("Seleccione una opcion: "))
    if opcion==1:
        print("Eligio la opcion 1")
    elif opcion==2:
        print("Se eligio la opcion 2")
    elif opcion==3:
        print("Se eligio la opcion 3")
    elif opcion==4:
        print("Saliendo")
        control=False
        break
    else:
        print("Error elija una opcion correcta")



