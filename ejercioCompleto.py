#Realizar un programa PARA UN CAJERO
#Donde se tenga la clase padre Usuario
#se debera catologar por tipos de usuario
#Usuario Normal
#Usuario Preferenciasl
#Usuario Vip
#ademas la clase padre tendra 3 acciones
#Retirar, Depositar, VerSaldo
#Propiedades de la clase padre (nombre,ci,saldo)
#Para cada tipo de usuario aplicar restricciones de retiro
#UN (limite=1000bs al dia)
#UP (limite=5000bs al dia)
#UV (ilimintado)
#Crear un menu para que el usuario pueda acceder
#PASO 1. CREAR CLASE PADRE
class Usuario:
    #Definir el constructor
    def __init__(self,nombre,ci,saldo):
        self.nombre=nombre
        self.ci=ci
        self.saldo=saldo
    #Paso 2. Definir las acciones de la clase
    def verSaldo(self):
        print(f"El saldo actual es {self.saldo}Bs - Usuario: {self.nombre}")
    def depositar(self,monto):
        #Para depositar en la cuenta lo minimo sera 1
        if monto>0:
            self.saldo=self.saldo+monto
            print(f"Deposito realizado correctamente... Saldo Actual {self.saldo}")
        else:
            print("Error verifique el monto a ingresar...")
    def retirar(self,monto):
        if monto>self.saldo:
            print("Saldo insuficiente no se pudo realizar la operacion...")
        else:
            self.saldo=self.saldo-monto
            print(f"Retiro Realizado correctamente  de {monto}Bs - Saldo Actual {self.saldo}Bs")

#usuario1=Usuario("Kevin",1234567,0)
#usuario1.verSaldo()
#usuario1.depositar(1000)
#usuario1.retirar(1001)

#monto=float(input("Ingrese el monto a depositar: "))
#usuario1.depositar(monto)

#CATOLOGAR A LOS USUARIOS (UN, UP, UV)
class UsuarioNormal(Usuario):
    #Definir el constructor
    def __init__(self,nombre,ci,saldo,correo,direccion):
        #Heredar las propiedades de la clase padre
        #metodo super()
        super().__init__(nombre,ci,saldo) #Herencia de propiedades
        self.correo=correo #propiedades de la subclase
        self.direccion=direccion #propiedades de la subclase
        #variables nativas
        self.limite=1000
    #Accion a heredar  (Polimorfismo)
    def retirar(self,monto):
        #Aplicar las restriccion
        if monto>self.limite:
            print("Error alcanzo el limite de retiro...")
        elif monto>self.saldo:
            print("Saldo insuficiente...")
        else:
            self.saldo=self.saldo-monto
            print(f"Retiro Normal procesado - Saldo Actual {self.saldo}")

#usuarioN=UsuarioNormal("Juan",12445678,1050,"a@gmail.com","absc av xyz")
#usuarioN.retirar(200)
#usuarioN.retirar(1001)
#usuarioN.depositar(5000)

class UsuarioPreferencial(Usuario):
    def __init__(self,nombre,ci,saldo):
        super().__init__(nombre,ci,saldo)
        #Variable nativa
        self.limite=5000
    #acciones
    def retirar(self,monto):
        if monto>self.limite:
            print("Error alcanzo el limite de retiro...")
        elif monto>self.saldo:
            print("Saldo insuficiente...")
        else:
            self.saldo=self.saldo-monto
            print(f"Retiro Preferencial existoso - Saldo actual {self.saldo}Bs")

#usuarioP=UsuarioPreferencial("Jose",125458841,1500)
#usuarioP.retirar(5002)

class UsuarioVip(Usuario):
    def __init__(self,nombre,ci,saldo):
        super().__init__(nombre,ci,saldo)
        self.ilimitado=True
    def retirar(self,monto):
        if self.ilimitado:
            if monto>self.saldo:
                print("Saldo insuficiente")
            else:
                self.saldo=self.saldo-monto
        else: 
            print("Ya no es un usuario Vip")

