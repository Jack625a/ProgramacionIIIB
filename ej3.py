#DADO UNA LISTA DE EDADES(15,20,13,11,45,25,23) 
# VERIFICAR QUIENES SON MAYORES DE EDAD

edades=[15,20,13,11,45,25,23]
for edad in edades:
    if edad>=18:
        print("es mayor de edad")
    else:
        print("es menor de edad")