#Programacion Orientda a Objetos
#1. clases class
#2 propiedades, atributos self
#3. acciones, metodos def 
#4. objetos 

#CLASE PERSONA (clase padre)
#PROPIEDADES #Nombre, edad, altura, ci
#metodos/acciones caminar() comer() dormir()
#Objetos persona1=("Juan",19,)

#SUBCLASES ESTUDIANTES (clases hijos)
#PROPIEDADES codEstudiante, carrera, semestre, 
#acciones estudiar() jugar()

#SUBCLASE DOCENTES 
#PROPIEDADES profesion, carrera, 
#acciones evaluar() revisarExamen()

#SINTAXIS BASICA POO
#CLASE CLASS
#PROPIEDADES SELF
#ACCIONES DEF

#Paso 1. Definir la clase (para definir el nombre de la clase iniciamos con Mayuscula)
class Persona:
    #Paso 2. Definir las propiedades de la clase
    #constructor
    def __init__(self,nombre,edad,altura,ci):
        #propiedades almacenarlos en variables
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
        self.ci=ci
    #PASO 3. DEFINIR LAS ACCIONES 
    def comer(self,comida):
        print(f"{self.nombre} Esta comiendo {comida}")

    def dormir(self):
        print(f"{self.nombre} Esta durmiendo")

    def caminar(self):
        print("esta caminando")


#Crear los objetos
persona1=Persona("Kevin",29,1.75,1234568)
persona2=Persona("Ana",25,1.65,4552216)

persona1.comer("Pan")
persona2.dormir()

#Crear la clase Estudiante
#HERENCIA
#SUBCLASE( HEREDAR ATRIBUTOS Y ACCIONES DE CLASEA PADRE)
#Paso 1. Definir la subclase 
class Estudiante(Persona):
    #crear el contructor
    def __init__(self,nombre,edad,altura,ci,codEstudiante,carrera,semestre):
        #Paso 2. HERENCIA DE ATRIBUTOS
        #super()
        super().__init__(nombre,edad,altura,ci) #heredar los atributps
        self.codEstudiante=codEstudiante
        self.carrera=carrera
        self.semestre=semestre

    #Paso 3. Definir las acciones Estudiante
    def estudiar(self):
        print(f"{self.nombre} esta estdudiando..")


estudiante1=Estudiante("Kevin",25,1.75,12345678,45451,"Ingenieria de Sistemas",6)
estudiante2=Estudiante()
estudiante1.dormir()
estudiante1.estudiar()
estudiante1.comer("Pan")