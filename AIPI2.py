print("Hola! Esta es la actividad integradora de programación Inicial de Colica, Toledo, Vallejos")
print('Por favor, ingresá un número, este es el bucle')


myList = []
for x in range(5):
    valor=int(input("Ingrese un numero: "))
    myList.append(valor)

print (myList)

suma_total = sum(myList)

promedio = sum(myList)/len(myList)

print ("La suma total es de: ", suma_total)

print ("El promedio es de: ", promedio)
