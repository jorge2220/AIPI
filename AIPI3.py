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
