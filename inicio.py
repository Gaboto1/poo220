lista=[22,44,1.2,"hola",'Mundo']
tupla=(22,44,1.2,"hola",'Mundo')
print(lista)
print(tupla)
lista.append("INSERTANDO")
print(lista)
lista.insert(2,"POSICION 2")
print(lista)
#soy un comentario
conjunto=[]

i=0
while i<10:
    persona1={}
    print(i)
    i=i+1
   # persona1={"nombre":"juan"+str(i),"apellido":"soto"+str(i)}
    persona1["nombre"] = input("escribe el nombre: ")
    persona1["apellido"] = input("escribe el apellido: ")

    conjunto.append(persona1)
    print(conjunto)
for z in conjunto:
    print(z["nombre"]+" "+z["apellido"])

