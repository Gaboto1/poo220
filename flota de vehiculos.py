from winsound import PlaySound


class Auto:
    def __init__(self,Velocidad,Kilometraje,marca ):
        self.Velocidad=Velocidad
        self.Kilometraje=Kilometraje
        self.marca=marca

    def getVelocidad(self):
        return self.Velocidad
    def getKilometraje(self):
        return self.Kilometraje
    def getmarca(self):
        return self.marca

    def mostrarAuto(self):
        print("\nVelocidad: "+ self.Velocidad()+"\nKilometraje: "+str(self.getKilometraje()+"\nMarca: "+self.getmarca()))

Velocidad=input("Ingrese velocidad del auto: ")
Kilometraje=input("Ingre kilometraje: ")
marca=input("Ingrese la marca del auto: ")

a=Auto(Velocidad,Kilometraje,marca)
a.mostrarAuto
print(a)

sumar = lambda x,y: x+y
print(sumar(2,3))



