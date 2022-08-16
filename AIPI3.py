print("Hola! Esta es la actividad integradora de programación Inicial de Colica, Toledo y Vallejos")

list=[]; #Se define una lista llamada list.
for i in range(0,5,1): #Se crea un bucle para el ingreso de cada valor por consola y se ingresa dicho valor en la lista 'list'.
    list.append(int(input('Ingrese un número: ')));

# se define una función suma donde recibe como parámetro la lista, se ingresa un bucle con una condición donde se lee la longitud de la lista y se itera en la misma,
# define una variable en forma local para guardar el valor de la sumatoria de los valores en las posiciones de la lista, luego se retorna un texto junto al resultado.
def suma(list):
    x=0;
    for i in range(len(list)):
        x += list[i];
    return x
    
# se define una función prom donde recibe la lista como parámetro y luego con un bucle se itera la longitud de la lista donde se guarda la sumatoria de todos los valores y se los divide por la longuitud de la lista,
# se retorna el valor del promedio junto a un texto. 
def prom(list):
    res=0
    for i in range(0,len(list),1):
        res+=list[i]
    total= res/len(list)
    return total

#Se define una función max donde se recibe la lista como parámetro y se itera en la misma junto a una condición donde se valida si el valor en la variable max es igual o mayor a la 
# posición de la lista, se va actualizando el valor de la variable si es mayor al anterior y se muestra un texto junto al valor máximo encontrado. 
def max(list):
    max=0
    for i in range(0,len(list),1):
        if(list[i] >= max):
            max=list[i]
    return max
    
