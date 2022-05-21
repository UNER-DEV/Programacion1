from modules.utils import *
from collections import OrderedDict

# --------------------------------------------------------------------------------------------- 
# 5.Escriba un programa Python que solicite al usuario el ingreso de numeros enteros. 
# Cuando el usuario ingrese la palabra [fin] el programa debera concluir con la carga de datos.
#  Cada uno de los numeros ingresados por el usuario debera ser almacenado en una lista.
#  A continuacion, realice las siguientes tareas:
    # a. Determinar el maximo.
    # b. Obtener segundo valor maximo. Es decir el que le sigue al maximo.
    # c. Determinar el minimo.
    # d. Calcular la multiplicacion de todos los numeros de la lista.
    # e. Contar los valores pares e impares.
    # f. Remover los enteros repetidos.
# --------------------------------------------------------------------------------------------- 

clear()

lista_enteros=[]

print('A continuacion debera ingresar un numero y podra hacerlo las veces que quiera.\nPara finalizar escriba la palabra [fin].')

while True:
    entero=normalizar(input('\n\nIngrese un numero entero o escriba [fin] >> '))
    clear()
    if(entero == 'fin'):
        break
    elif entero.isnumeric():
        lista_enteros.append(int(entero))
        print(f'Se ha agregado correctamente el numero {entero}')
    
lista_enteros = sorted(lista_enteros)

sin_repetidos = list(OrderedDict.fromkeys(lista_enteros))
# otra opc => sin_repetidos = quitarRepetidos(lista_enteros)

par = 0
impar = 0
total_multiplicacion = 1
for i in lista_enteros:
    total_multiplicacion *=i
    if(EsParOImpar(i)):
        par+=1     
    else:
        impar+=1

print(f'\n >> Todos los numeros ingresados son {lista_enteros}\n')

print(f' >> El numero mas alto de esa lista es {max(sin_repetidos)}, el segundo numero mas alto es {sin_repetidos[-2]} y el numero mas bajo es {min(sin_repetidos)}.\n')

print(f' >> Todos los numeros multiplicados dan como resultado {total_multiplicacion}.\n')

print(f' >> Hay {par} numeros pares y {impar} numeros impares en la lista.\n')

print(f' >> La lista final, sin numeros repetidos, es la siguiente: {sin_repetidos}\n')

# --------------------------------------------------------------------------------------------- 

if(checkInputSiNo('Desea volver al MENU PRINCIPAL? >> ') == 'si'):
    exec(open(rutaMenu).read())
else:
    print(f'\n[Este programa ha finalizado]\n')
    exit()
