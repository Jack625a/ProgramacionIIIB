#CREAR LA CLASE AUTOMOVIL
#SUBCLASE AUTOMOVILELECTRICO
class Automovil:
    def __init__(self,marca,modelo,color,placa):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.placa=placa
    def frenar(self):
        print(f"{self.marca} esta frenando el auto")
    def acelerar(self):
        print(f"{self.marca} esta acelerando el auto")

#Subclase
class AutoElectrico(Automovil):
    def __init__(self,marca,modelo,color,placa,bateria):
        super().__init__(marca,modelo,color,placa)
        self.bateria=bateria
    def cargarEnergia(self):
        print(f"{self.marca} esta cargando la bateria....")

auto1=AutoElectrico("Tesla",2025,"Plomo","452f5",100)
auto1.acelerar()
auto1.cargarEnergia()