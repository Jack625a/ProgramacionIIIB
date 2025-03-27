#Comunicacion entre clases padre
#1. Clases intermedias (puente de comunicacion)
class Persona:
    def __init__(self,nombre,ci,edad):
        self.nombre=nombre
        self.edad=edad
        self.ci=ci
    def comer(self):
        print("Esta comiendo")
    def inscribirse(self,sistema):
        print("Solicitud de inscripsion")
        self.sistema=sistema

#Clase padre
class Universidad:
    def __init__(self,sistema):
        self.sistema=sistema
    
    #ACCIONES DE LA UNIVERSISAD
    def procesarSolicitud(self):
        print("Universidad esta procesando su solicitud...")


#CLASE INTERMEDIA (PUENTE DE COMUNICACION)
class SistemaRegistroUniversidad:
    def __init__(self,usuario,contraseña):
        self.usuario=usuario
        self.contraseña=contraseña
        self.mensaje=""
    #ACCIONES DE LA CLASE
    def enviar(self,mensaje):
        print('Mensaje enviado')
        self.mensaje=mensaje
    def recibir(self):
        print("Mensaje recibido")
        return self.mensaje
    

#Probar los objetos de la clase
sistema=SistemaRegistroUniversidad("abc",123)
estudiante1=Persona("Kevin",1244555,29)
udabol=Universidad(sistema)
estudiante1.inscribirse(sistema)
sistema.recibir()