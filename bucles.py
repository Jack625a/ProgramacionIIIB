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


