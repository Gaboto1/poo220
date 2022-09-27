istancia=0
ruedas=int(input("\nCuántas ruedas tiene el vehículo?: "))
print("Donde se encuentra el veiculo?")
print("( x , y )")
x=int(input("Ingrese x: "))
y=int(input("Ingrese y: "))
ubicacion = [x,y]
velocidad=int(input("A que velocidad va el vehículo?: "))
on="Encendido"
horas=velocidad/60
def salida():
    print("El vehículo tiene "+str(ruedas)+ " ruedas")
    print("El vehículo está en la posicion "+str(ubicacion)+ " del GPS")
    print("El vehículo va a "+str(velocidad)+ " km/h")
    print("Estado del auto: "+str(on))
def acelerar():
    global velocidad
    global on
    if on=="Encendido":
        velocidad=int(velocidad)+10
        print("El vehículo ha acelerado a "+str(velocidad)+" km/h")
    else:
        print("El vehiculo se encuentra apagado")
    sino()
def apagado():
    global on
    pren=int(input("Que desea hacer? \n1.Apagar \n2.Encender \n Opcion: "))
    if pren==1:
        on="Apagado"
    elif pren==2:
        on="Encendido"
    print("\nEstado actual vehiculo: "+str(on))
    sino()
def sino():
    global opc
    sino=str(input("Desea volver al menu? (y/n): "))
    if sino=="n":
        opc=9
def freno():
    global on
    global velocidad
    if on=="Encendido" and velocidad<=89:
        print("El vehiculo freno")
        velocidad=0
    if on=="Encendido" and velocidad>=90:
        print("El vehiculo freno")
        velocidad=0
    if on=="Apagado":
        print("Has generado un error en el tiempo")
        print("El vehiculo esta apagado")
    sino()
def distanciaRe():
    global distancia
    global velocidad
    global ubicacion
    global ubicacion1
    global x
    global y
    distancia=velocidad*horas
    x=(x+distancia)
    y=(x+distancia)
    ubicacion1 = [x,y]
    print("Kilometros recorridos: "+str(distancia)+" km")
    print("Tiempo en carretera: "+str(horas)+" hr")
    print("Ubicacion vehiculo")
    print("Inicio: "+str(ubicacion))
    print("Final: "+str(ubicacion1))
    opc=5
opc=0
while((opc)!=9):
    print("Elija opcion a realizar")
    opc = int(input("1.Mostrar datos \n2.Acelerar \n3.Encender/Apagar \n4.Frenar \n5.Distancia \n9.Salir \nOpcion: "))
    con=opc
    if(opc==1):
        salida()
    if(opc==2):
        acelerar()
    if(opc==3):
        apagado()
    if(opc==4):
        freno()
    if(opc==5):
        distanciaRe()
if distancia!=0:
    print("Buen viaje")
    print("Km : ")
    print("tiempo: ")
    print("Ubicacion : ["+" "+"]")
else:
    print("Hasta Luego")

