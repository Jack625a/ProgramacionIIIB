#SUBCLASE-> HERENCIA DE ATRIBUTOS Y METODOS DE LA CLASE PADRE
#HERENCIA OBTENER LOS ATRIBUTOS Y ACCIONES (super())
#class(ClasePadre)

#Paso 1. Crear la clase padre
class Persona:
    #Paso 2. Definir el constructor
    def __init__(self,nombre,edad,ci,celular):
        self.nombre=nombre
        self.edad=edad
        self.ci=ci
        self.celular=celular
    #Paso 3. Crear las acciones o metodos
    def comer(self,comida):
        print(f"{self.nombre} esta comiendo {comida}")
    def dormir(self):
        print(f"{self.nombre} esta durmiendo...")


#Paso 4. Crear los objetos de la clase
#NOTA: LOS OBJETOS ESTAN POR FUERA DE LA CLASE

persona1=Persona("Kevin",29,1234567,654122142)
persona2=Persona("Juan",24,745662,65544112)

persona1.comer("Pan")
persona2.dormir()
persona2.comer("Galletas")


#SUBCLASE
#SUBCLASE ESTUDIANTE
#Paso 1. Definir la subclase
#NOTA: PARA DEFINIR UNA SUBCLASE SE UTILIZA class(ClasePadre)
class Estudiante(Persona):
    #Paso 2. Definir el constructor
    def __init__(self,nombre,edad,ci,celular,carrera,codigoEstudiante):
        #Paso 3. Realizar la herencia de atributos de la clase padre
        #super().
        super().__init__(nombre,edad,ci,celular)
        #Paso 4. definir los paremtros de la subclase estudiante
        self.carrera=carrera
        self.codigoEstudiante=codigoEstudiante
    #Paso 5. ACCIONES DE LA SUBCLASE
    def estudiar(self):
        print(f"{self.nombre} esta estudiando...")
    def darExamen(self):
        print(f"{self.nombre} esta dando examen...")

#Paso 6. crear los objetos de la subclase
estudiante1=Estudiante("Jose",18,1234555,71889111,"Ingenieria de Sistemas",456789)
estudiante2=Estudiante("Ana",21,74125896,65241784,"Medicina",741586)
estudiante1.comer("Galletas")
estudiante1.estudiar()
estudiante1.darExamen()
estudiante2.dormir()
