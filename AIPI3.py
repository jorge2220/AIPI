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
    
#Se realiza lo mismo que en la función anterior pero se cambia la condición, donde en lugar de buscar el valor máximo se busca el mánimo, habiendo definido la variable min como 
# la posición 0 de la lista para usar de refrente. 
def min(list):
    min=list[0]
    for i in range(0,len(list),1):
        if(list[i] <= min):
            min=list[i];
    return min


# Se hace un print con la llamada de la función y se ingresa la lista como valor a operar.
print("La suma es:", suma(list))
print("El promedio es:", prom(list))
print("El valor máximo es:", max(list))
print("El valor mínimo es:", min(list))




# Este es el ejercicio anterior
# numero1 = int(input("Ingrese el primer número: "))
# numero2 = int(input("Ingrese el segundo número: "))
# numero3 = int(input("Ingrese el tercer número: "))
# numero4 = int(input("Ingrese el cuarto número: "))
# numero5 = int(input("Ingrese el quinto número: "))

# myList = [ numero1, numero2, numero3, numero4, numero5]

# sumatotal = (numero1 + numero2 + numero3 + numero4 + numero5)

# promedio = (sumatotal/5)

# numero_maximo = max(myList)

# numero_minimo = min(myList)

# print (myList)

# print (sumatotal)

# print ("El promedio es:", promedio)

# print ("El numero maximo es:", numero_maximo)

# print ("El numero minimo es:", numero_minimo)
